import argparse
import html
import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import quote, urlsplit

import requests
from bs4 import BeautifulSoup


def load_config(path: Path) -> dict:
    with path.open(encoding="utf-8") as file:
        config = json.load(file)

    required = (
        "pageId",
        "tableColumns",
        "targetFiles",
        "sectionStart",
        "sectionEnd",
    )
    missing = [key for key in required if key not in config]
    if missing:
        raise ValueError(f"Missing required config keys: {', '.join(missing)}")

    if config["sectionStart"] == config["sectionEnd"]:
        raise ValueError("sectionStart and sectionEnd cannot be the same")

    if not isinstance(config["tableColumns"], list) or not config["tableColumns"]:
        raise ValueError("tableColumns must be a non-empty list")
    if not isinstance(config["targetFiles"], list) or not config["targetFiles"]:
        raise ValueError("targetFiles must be a non-empty list")

    return config


def fetch_page_html(page_id: str) -> str:
    cloud_id = os.environ.get("CONFLUENCE_CLOUD_ID")
    email = os.environ.get("CONFLUENCE_EMAIL")
    token = os.environ.get("CONFLUENCE_API_TOKEN")
    missing = [
        name
        for name, value in (
            ("CONFLUENCE_CLOUD_ID", cloud_id),
            ("CONFLUENCE_EMAIL", email),
            ("CONFLUENCE_API_TOKEN", token),
        )
        if not value
    ]
    if missing:
        raise RuntimeError(
            f"Missing required environment variables: {', '.join(missing)}"
        )

    url = (
        f"https://api.atlassian.com/ex/confluence/{cloud_id}"
        f"/wiki/api/v2/pages/{page_id}?body-format=storage"
    )

    response = requests.get(
        url,
        auth=(email, token),
        headers={"Accept": "application/json"},
        timeout=30,
    )

    if response.status_code == 401:
        raise RuntimeError("Unauthorized: Check your email and API token")
    if response.status_code == 403:
        raise RuntimeError("Forbidden: Check your permissions for this page")
    if response.status_code == 404:
        raise RuntimeError("Not Found: The requested page does not exist")

    response.raise_for_status()
    data = response.json()

    try:
        return data["body"]["storage"]["value"]
    except (KeyError, TypeError) as error:
        raise RuntimeError(
            "Unexpected response format: 'body.storage.value' not found"
        ) from error


def _cell_text(cell) -> str:
    for line_break in cell.find_all("br"):
        line_break.replace_with("\n")
    for item in cell.find_all("li"):
        item.insert_before("\n")
    return " ".join(cell.get_text(" ", strip=True).split())


def _markdown_text(value: str, in_table_cell: bool = False) -> str:
    value = html.escape(value, quote=False)
    value = value.replace("\\", "\\\\").replace("[", r"\[").replace("]", r"\]")
    if in_table_cell:
        value = value.replace("|", "&#124;")
    return value


def _safe_markdown_url(value: str) -> str | None:
    value = value.strip()
    try:
        parsed = urlsplit(value)
    except ValueError:
        return None

    if parsed.scheme:
        if parsed.scheme.casefold() not in ("http", "https") or not parsed.netloc:
            return None
    elif parsed.netloc:
        return None

    return quote(value, safe=":/?#[]@!$&'*+,;=%-._~")


def _endpoint_list(cell) -> list[str]:
    items = [_cell_text(item) for item in cell.find_all("li")]
    if not items:
        copy = BeautifulSoup(str(cell), "html.parser")
        paragraphs = copy.find_all("p")
        containers = paragraphs or [copy]
        for container in containers:
            for line_break in container.find_all("br"):
                line_break.replace_with("\uE000")
            text = container.get_text(" ", strip=True)
            items.extend(
                " ".join(part.split())
                for part in text.split("\uE000")
                if part.strip()
            )
    return [item for item in items if item]


def _path_cell(value: str) -> str:
    value = value.strip()
    if not value:
        return "n/a"
    if value.lower() in ("n/a", "tbc"):
        return _markdown_text(value, in_table_cell=True)
    return f"<code>{html.escape(value).replace('|', '&#124;')}</code>"


def _error_type_cell(value: str) -> str:
    value = value.strip()
    if not value:
        return ""
    if value.startswith("<a "):
        anchor = BeautifulSoup(value, "html.parser").find("a")
        if anchor is None:
            return _markdown_text(value, in_table_cell=True)
        label = anchor.get_text(" ", strip=True)
        href = _safe_markdown_url(str(anchor.get("href", "")))
        if href:
            return (
                '<a target="_blank" rel="noopener noreferrer" '
                f'href="{html.escape(href, quote=True)}">'
                f'{html.escape(label).replace("|", "&#124;")}</a>'
            )
        return _markdown_text(label, in_table_cell=True)
    if value.startswith("http://") or value.startswith("https://"):
        soup = BeautifulSoup(value, "html.parser")
        value = soup.get_text(" ", strip=True)
    href = (
        "https://problem.api.bunnings.com.au/?type="
        + quote(value, safe="")
    )
    return (
        '<a target="_blank" rel="noopener noreferrer" '
        f'href="{html.escape(href, quote=True)}">'
        f'{html.escape(value).replace("|", "&#124;")}</a>'
    )


def _endpoint_cell(cell) -> str:
    endpoints = _endpoint_list(cell) or ["TBC"]
    list_items = "".join(
        f"<li>{html.escape(endpoint).replace('|', '&#124;').replace(' ', '&nbsp;', 1)}</li>"
        for endpoint in endpoints
    )
    return f"<details><summary>End Points:</summary><ul>{list_items}</ul></details>"


def _normalize_header(value: str) -> str:
    value = re.sub(r"\([^)]*\)", "", value.casefold())
    normalized = re.sub(r"[\s_\-/]+", "", value)
    return {
        "endpoints": "endpoint",
        "businessrules": "businessrule",
    }.get(normalized, normalized)


def _inline_markdown(node, in_table_cell: bool = False) -> str:
    if getattr(node, "name", None) is None:
        return _markdown_text(str(node), in_table_cell)

    name = (node.name or "").lower()
    if name == "br":
        return "<br>" if in_table_cell else "\n"

    content = "".join(
        _inline_markdown(child, in_table_cell) for child in node.children
    )
    if name in ("strong", "b"):
        return f"**{content}**"
    if name in ("em", "i"):
        return f"*{content}*"
    if name in ("code", "tt"):
        return f"`{content}`"
    if name == "a" and node.get("href"):
        href = _safe_markdown_url(str(node["href"]))
        return f"[{content}](<{href}>)" if href else content
    if name in ("ul", "ol"):
        items = [
            "- " + _inline_markdown(item, in_table_cell).strip()
            for item in node.find_all("li", recursive=False)
        ]
        separator = "<br>" if in_table_cell else "\n"
        return separator.join(items)
    if name == "li":
        return content
    if name == "p" and in_table_cell:
        return content + "<br>"
    return content


def _table_rows(table):
    return table.find_all("tr")


def _table_header_labels(table) -> list[str]:
    for row in _table_rows(table):
        cells = row.find_all(["th", "td"], recursive=False)
        if any(cell.name == "th" for cell in cells):
            return [_cell_text(cell) for cell in cells]
    return []


def _error_code_table_indexes(table, columns: list[str]):
    configured_columns = [column.strip().casefold() for column in columns]
    for header_index, row in enumerate(_table_rows(table)):
        header_cells = row.find_all(["th", "td"], recursive=False)
        headers = [_cell_text(cell).casefold() for cell in header_cells]
        normalized_headers = [_normalize_header(header) for header in headers]
        indexes = {
            column: normalized_headers.index(_normalize_header(column))
            for column in configured_columns
            if _normalize_header(column) in normalized_headers
        }
        if "error code" in indexes:
            in_prod_index = (
                normalized_headers.index("inprod")
                if "inprod" in normalized_headers
                else None
            )
            return header_index, indexes, in_prod_index
    return None, None, None


def _in_prod_status(value: str) -> str | None:
    match = re.match(r"^\s*(yes|no|removed)\b", value, flags=re.IGNORECASE)
    return match.group(1).casefold() if match else None


def _constant_names_from_markdown(content: str) -> dict[str, str]:
    constant_names = {}
    lines = content.splitlines()
    for index, line in enumerate(lines):
        if not line.strip().startswith("|"):
            continue

        headers = [
            html.unescape(value).replace("\xa0", " ").strip().casefold()
            for value in line.strip().strip("|").split("|")
        ]
        normalized_headers = [
            re.sub(r"[\s_\-/]+", "", value) for value in headers
        ]
        if "constantname" not in normalized_headers:
            continue

        constant_index = normalized_headers.index("constantname")
        code_index = next(
            (
                header_index
                for header_index, header in enumerate(normalized_headers)
                if header in ("errorcode", "shorterrorcode")
            ),
            None,
        )
        if code_index is None:
            continue

        for row in lines[index + 1:]:
            if not row.strip().startswith("|"):
                break
            cells = [
                value.strip() for value in row.strip().strip("|").split("|")
            ]
            if (
                len(cells) <= max(code_index, constant_index)
                or re.fullmatch(r":?-{3,}:?", cells[0])
            ):
                continue

            code = html.unescape(cells[code_index]).strip()
            name = html.unescape(cells[constant_index]).strip()
            if code and name:
                constant_names[code.casefold()] = name

    return constant_names


def _render_error_code_table(
    table, columns: list[str], constant_names: dict[str, str] | None = None
) -> tuple[bool, str, bool, int]:
    header_index, indexes, in_prod_index = _error_code_table_indexes(table, columns)
    if indexes is None:
        return False, "", False, 0
    if in_prod_index is None:
        return True, "", True, 0

    output_columns = [
        ("error code", "Short&nbsp;error&nbsp;code"),
        ("business rule", "Business Rules"),
        ("error message", "Message"),
        ("rule type", "Error type"),
        ("path", "Path"),
        ("endpoint", "End Points"),
    ]
    output_columns = [
        column for column in output_columns if column[0] in indexes
    ]
    table_rows = _table_rows(table)
    rows = []
    unrecognized_statuses = 0

    for row in table_rows[header_index + 1:]:
        cells = row.find_all(["th", "td"], recursive=False)
        if len(cells) <= max(max(indexes.values()), in_prod_index):
            continue

        status = _in_prod_status(_cell_text(cells[in_prod_index]))
        if status not in ("yes", "no"):
            if status is None:
                unrecognized_statuses += 1
            continue

        values = {
            column: _cell_text(cells[indexes[column]])
            for column in indexes
        }
        if not values.get("error code"):
            continue

        endpoint = (
            _endpoint_cell(cells[indexes["endpoint"]])
            if "endpoint" in indexes
            else ""
        )
        rows.append((values, endpoint))

    if constant_names and any(
        values["error code"].casefold() in constant_names
        for values, _ in rows
    ):
        output_columns.insert(1, ("constant name", "Constant Name"))

    rendered_rows = []
    for values, endpoint in rows:
        output_cells = []
        for key, _ in output_columns:
            if key == "constant name":
                output_cells.append(
                    _markdown_text(
                        constant_names.get(values["error code"].casefold(), ""),
                        in_table_cell=True,
                    )
                )
            elif key == "path":
                output_cells.append(_path_cell(values[key]))
            elif key == "rule type":
                output_cells.append(_error_type_cell(values[key]))
            elif key == "endpoint":
                output_cells.append(endpoint)
            else:
                output_cells.append(
                    _markdown_text(values[key], in_table_cell=True)
                )
        rendered_rows.append("| " + " | ".join(output_cells) + " |")

    if unrecognized_statuses:
        print(
            f"Skipped {unrecognized_statuses} error-code row(s) with an "
            "unrecognized In Prod value.",
            file=sys.stderr,
        )

    if not rendered_rows:
        return True, "", False, unrecognized_statuses

    header = "| " + " | ".join(label for _, label in output_columns) + " |"
    separator = "| " + " | ".join("--------" for _ in output_columns) + " |"
    return True, "\n".join([header, separator, *rendered_rows]), False, unrecognized_statuses


def _render_markdown_table(table) -> str:
    table_rows = _table_rows(table)
    if not table_rows:
        return ""

    header_index = next(
        (
            index
            for index, row in enumerate(table_rows)
            if row.find_all("th", recursive=False)
        ),
        0,
    )
    header_cells = table_rows[header_index].find_all(
        ["th", "td"], recursive=False
    )
    if not header_cells:
        return ""

    headers = [
        _markdown_text(_cell_text(cell), in_table_cell=True)
        for cell in header_cells
    ]
    rows = []
    for row in table_rows[header_index + 1:]:
        cells = row.find_all(["th", "td"], recursive=False)
        if len(cells) != len(headers):
            continue
        values = []
        for cell in cells:
            value = _inline_markdown(cell, in_table_cell=True).strip()
            value = re.sub(r"(?:<br>)+$", "", value).strip()
            values.append(value)
        rows.append("| " + " | ".join(values) + " |")

    if not rows:
        return ""
    header = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join("--------" for _ in headers) + " |"
    return "\n".join([header, separator, *rows])


def _plain_text(node) -> str:
    return " ".join(node.get_text(" ", strip=True).split())


def _section_marker_title(element) -> str | None:
    text = _plain_text(element)
    match = re.match(
        r"^(?:\d+\s*[.)]\s*)?Section\s*:\s*(.+)$",
        text,
        flags=re.IGNORECASE,
    )
    return match.group(1).strip() if match else None


def _test_case_parent(test_section, error_sections):
    referenced_codes = set(
        re.findall(
            r"\bE-[A-Z0-9]+-\d+\b",
            " ".join(
                (
                    test_section["marker_title"],
                    test_section["heading"],
                    *test_section["parts"],
                )
            ),
            flags=re.IGNORECASE,
        )
    )
    matches = [
        section
        for section in error_sections
        if referenced_codes.intersection(section["error_codes"])
    ]
    if len(matches) == 1:
        return matches[0]

    candidate_names = []
    for value in (test_section["marker_title"], test_section["heading"]):
        candidate = re.sub(r"\([^)]*\)", "", value)
        candidate = re.sub(
            r"^\s*subsection\s*:\s*", "", candidate, flags=re.IGNORECASE
        )
        candidate = re.sub(
            r"^\s*test\s+cases?\s*(?:for\s+)?",
            "",
            candidate,
            flags=re.IGNORECASE,
        )
        candidate = re.sub(
            r"\btest\s+cases?\b.*$",
            "",
            candidate,
            flags=re.IGNORECASE,
        ).strip(" :-")
        if candidate:
            candidate_names.append(candidate.casefold())

    for candidate in sorted(set(candidate_names), key=len, reverse=True):
        matches = [
            section
            for section in error_sections
            if candidate in section["heading"].casefold()
            or section["heading"].casefold() in candidate
        ]
        if len(matches) == 1:
            return matches[0]
    return None


def _metadata_label_values(element) -> list[tuple[str, str]] | None:
    text = _inline_markdown(element).strip()
    matches = list(
        re.finditer(
            r"\*{0,2}(heading|description)\*{0,2}\s*:",
            text,
            flags=re.IGNORECASE,
        )
    )
    if not matches or text[:matches[0].start()].strip():
        return None

    metadata = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        value = text[match.end():end].strip()
        value = re.sub(
            r"^(?:\s*<br\s*/?>\s*)+", "", value, flags=re.IGNORECASE
        )
        metadata.append(
            (match.group(1).casefold(), re.sub(r"\s+", " ", value).strip())
        )
    return metadata


def _clean_section_heading(value: str) -> str:
    value = re.sub(r"^`+(.*?)`+$", r"\1", value.strip())
    return re.sub(r"^#{1,6}\s*", "", value).strip()


def render_markdown_sections(
    page_html: str,
    columns: list[str],
    constant_names: dict[str, str] | None = None,
) -> str:
    configured_columns = [column.strip().casefold() for column in columns]
    soup = BeautifulSoup(page_html, "html.parser")
    sections = []
    current_section = None
    current_test_section = None
    in_test_cases = False
    missing_in_prod_sections = []
    found_headings = []
    found_table_headers = []

    def start_section(marker_title: str):
        return {
            "marker_title": marker_title,
            "heading": marker_title,
            "heading_is_markdown": False,
            "parts": [],
            "is_test_case_section": "test case" in marker_title.casefold(),
            "has_error_table": False,
            "has_included_error_rows": False,
            "has_test_case_table": False,
            "error_codes": set(),
        }

    def finish_test_section():
        nonlocal current_test_section
        if current_test_section is not None:
            sections.append(current_test_section)
            current_test_section = None

    for element in soup.find_all(["h1", "h2", "h3", "h4", "p", "table"]):
        if element.find_parent("table") is not None:
            continue

        if element.name in ("h1", "h2", "h3", "h4"):
            heading_text = _plain_text(element)
            if heading_text:
                found_headings.append(f"{element.name}: {heading_text}")
        elif element.name == "table":
            found_table_headers.append(_table_header_labels(element))

        if element.name in ("h2", "h3", "h4"):
            marker_title = _section_marker_title(element)
            if marker_title:
                finish_test_section()
                if current_section is not None:
                    sections.append(current_section)
                current_section = start_section(marker_title)
                in_test_cases = "test case" in marker_title.casefold()
                continue

            if element.name == "h2":
                finish_test_section()
                if current_section is not None:
                    sections.append(current_section)
                current_section = start_section(_plain_text(element))
                in_test_cases = "test case" in current_section["heading"].casefold()
                continue

            if current_section is not None:
                heading = re.sub(r"\s+", " ", _inline_markdown(element)).strip()
                if "test case" in heading.casefold():
                    finish_test_section()
                    current_test_section = start_section(_plain_text(element))
                    current_test_section["is_test_case_section"] = True
                    current_test_section["parent_section"] = current_section
                    in_test_cases = True
                else:
                    finish_test_section()
                    current_section["parts"].append(f"### {heading}")
                    in_test_cases = False
                continue

        content_section = current_test_section or current_section
        if content_section is None:
            continue

        if element.name == "p":
            metadata = _metadata_label_values(element)
            if metadata:
                for label, value in metadata:
                    if label == "heading":
                        if value:
                            heading = _clean_section_heading(value)
                            content_section["heading"] = heading
                            content_section["heading_is_markdown"] = True
                            in_test_cases = "test case" in heading.casefold()
                            if in_test_cases:
                                content_section["is_test_case_section"] = True
                    elif value:
                        content_section["parts"].append(value)
                continue

            paragraph = re.sub(r"\s+", " ", _inline_markdown(element)).strip()
            if paragraph:
                content_section["parts"].append(paragraph)
        elif element.name == "table":
            is_error_table, rendered, missing_in_prod, _ = _render_error_code_table(
                element, configured_columns, constant_names
            )
            if is_error_table:
                content_section["has_error_table"] = True
                if missing_in_prod:
                    missing_in_prod_sections.append(content_section["heading"])
                if rendered:
                    content_section["parts"].append(rendered)
                    content_section["has_included_error_rows"] = True
                    content_section["error_codes"].update(
                        re.findall(
                            r"\bE-[A-Z0-9]+-\d+\b",
                            rendered,
                            flags=re.IGNORECASE,
                        )
                    )
            elif in_test_cases:
                rendered = _render_markdown_table(element)
                if rendered:
                    content_section["parts"].append(rendered)
                    content_section["has_test_case_table"] = True

    finish_test_section()
    if current_section is not None:
        sections.append(current_section)

    if missing_in_prod_sections:
        raise ValueError(
            "An error-code table is missing its In Prod column; target file "
            "unchanged. Missing in: "
            + ", ".join(dict.fromkeys(missing_in_prod_sections)),
        )

    error_sections = [
        section for section in sections if section["has_error_table"]
    ]
    for section in sections:
        if section["is_test_case_section"]:
            if not section["has_test_case_table"]:
                continue
            parent = section.get("parent_section")
            if parent is None or not any(
                parent is candidate for candidate in error_sections
            ):
                parent = _test_case_parent(section, error_sections)
            if parent is None:
                raise ValueError(
                    "The related error-code section for a Test Cases section "
                    "could not be identified; "
                    "target file unchanged."
                )
            parent["parts"].append(f"### {section['heading']}")
            parent["parts"].extend(section["parts"])
            parent["has_test_case_table"] |= section["has_test_case_table"]

    rendered_sections = [
        section
        for section in sections
        if not section["is_test_case_section"]
        and (section["has_included_error_rows"] or section["has_test_case_table"])
    ]
    if not rendered_sections:
        headings = "; ".join(found_headings[:12]) or "(none)"
        table_headers = "; ".join(
            "[" + ", ".join(headers) + "]" if headers else "[no <th> header row]"
            for headers in found_table_headers[:12]
        ) or "(none)"
        raise ValueError(
            "No eligible error-code or test-case tables were found; "
            "target file unchanged. "
            f"Section headings found: {headings}. "
            f"Table headers found: {table_headers}."
        )

    rendered = []
    for section in rendered_sections:
        heading = section["heading"]
        if not section["heading_is_markdown"]:
            heading = _markdown_text(heading)
        rendered.append("\n\n".join([f"## {heading}", *section["parts"]]))
    return "\n\n".join(rendered)


def update_section(
    content: str, start_marker: str, end_marker: str, new_section: str
) -> str:
    if content.count(start_marker) != 1 or content.count(end_marker) != 1:
        raise ValueError("Each section marker must appear exactly once in the target file")

    start = content.index(start_marker) + len(start_marker)
    end = content.index(end_marker)
    if start > end:
        raise ValueError("The section markers are out of order")

    return (
        content[:start]
        + "\n"
        + new_section.strip()
        + "\n"
        + content[end:]
    )


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Sync structured Confluence voucher sections into Markdown."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path(__file__).resolve().parent.parent
        / "config"
        / "confluence-voucher-sync.json",
        help="Path to the sync configuration JSON file",
    )
    args = parser.parse_args(argv)

    try:
        config = load_config(args.config)
        repository_root = Path(__file__).resolve().parent.parent
        constant_name_source = config.get("constantNameSourceFile")
        constant_names = {}
        if constant_name_source:
            source_path = repository_root / constant_name_source
            source_content = source_path.read_text(encoding="utf-8")
            constant_names = _constant_names_from_markdown(source_content)

        page_html = fetch_page_html(str(config["pageId"]))
        markdown_sections = render_markdown_sections(
            page_html, config["tableColumns"], constant_names
        )
        if not markdown_sections.strip():
            raise ValueError(
                "Confluence page produced no Markdown sections; target file unchanged."
            )

        updates = []

        for target in config["targetFiles"]:
            target_path = repository_root / target
            content = target_path.read_text(encoding="utf-8")
            updated = update_section(
                content,
                config["sectionStart"],
                config["sectionEnd"],
                markdown_sections,
            )
            updates.append((target_path, updated))

        for target_path, updated in updates:
            target_path.write_text(updated, encoding="utf-8", newline="")
            print(f"Updated {target_path.relative_to(repository_root)}")
    except (OSError, ValueError, RuntimeError, requests.RequestException) as error:
        print(f"Confluence sync failed: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())