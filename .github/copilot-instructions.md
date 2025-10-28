# Copilot Instructions for Bunnings API Problems Repository

## Repository Purpose

This repository contains shared API problem definitions for Bunnings APIs, compliant with [RFC 7807 Problem Details for HTTP APIs](https://tools.ietf.org/html/rfc7807). The repository serves as a centralized documentation source for standardized error responses across all Bunnings APIs.

**Live Site:** https://problem.api.bunnings.com.au

## Repository Structure

- **Problem Definition Files**: Each problem type has two files:
  - `<problemName>.md` - Human-readable documentation with examples
  - `<problemName>.yaml` - OpenAPI schema definition
- **Error Code Documentation**: Detailed error code tables for different API domains:
  - `errorCodesBasket.md`, `errorCodesCheckout.md`, `errorCodesPayment.md`, etc.
- **Web Interface**: `index.html`, `index.xml`, `index.xsl` - Static website for browsing problems
- **Assets**: `bunnings-logo.png`, `CNAME` for GitHub Pages hosting

## Coding Standards

### YAML Files

1. **Indentation**: Use 2 spaces for indentation (never tabs)
2. **Schema Structure**: All problem schemas must follow RFC 7807 base structure:
   ```yaml
   <problemName>:
     type: object
     description: RFC 7807 compliant problem.
     required:
     - type
     properties:
       type:
         type: string
         format: uri
       title:
         type: string
       status:
         type: integer
       detail:
         type: string
       instance:
         type: string
         format: uri
   ```
3. **Extensions**: Additional properties can be added under `properties`, commonly including an `errors` object for detailed error information
4. **Formatting**: Maintain consistent spacing and alignment with existing files

### Markdown Files

1. **Headers**: Use proper heading hierarchy (H1 for title, H2 for sections)
2. **Problem Type Documentation Structure**:
   - Title (H1)
   - Brief description paragraph
   - "Problem Type" section (H2) with the problem URL
   - "Specification" section (H2) with YAML code block
   - Link to corresponding `.yaml` file
   - "Example" section (H2) with JSON code blocks
   - Optional "Links" section for error code references
3. **Error Code Tables**:
   - Use markdown tables with columns: `Short error code | Name | Description`
   - Use `&nbsp;` in headers to prevent wrapping: `Short&nbsp;error&nbsp;code`
   - Sort error codes alphanumerically
4. **Code Blocks**: Use triple backticks with language specification (```yaml, ```json)
5. **URLs**: Use the format `https://problem.api.bunnings.com.au?type=<problemName>`

## File Naming Conventions

- Problem definitions: `camelCase.md` and `camelCase.yaml` (e.g., `validationError.md`, `validationError.yaml`)
- Error code files: `errorCodes<Domain>.md` (e.g., `errorCodesCheckout.md`)
- Use descriptive, consistent names that match the problem type identifier

## RFC 7807 Compliance

All problem definitions MUST:
1. Include the required `type` property (URI reference)
2. Include standard optional properties: `title`, `status`, `detail`, `instance`
3. Use `application/problem+json` media type (documented in examples)
4. Follow the problem type URL pattern: `https://problem.api.bunnings.com.au?type=<problemName>`
5. Maintain consistency with the RFC 7807 specification

## Problem Type Extensions

Common extension patterns used in this repository:
- `errors` object containing field-specific error arrays or problem collections
- Error items typically include `code` (error code) and `message` (description)
- Two main patterns:
  1. Field-grouped errors (validation): `errors.<fieldName>[].{code, message}`
  2. Problem collections: `errors.problems[].{code, message}`

## Adding New Problems

When adding a new problem type:
1. Create both `.md` and `.yaml` files with matching names
2. Follow the existing documentation structure in the `.md` file
3. Ensure YAML schema is RFC 7807 compliant
4. Include at least one realistic JSON example
5. Update `index.xml` if needed to include the new problem in navigation
6. Use error codes following the pattern: `E-<DOMAIN>-<NUMBER>` (e.g., `E-CHK-0001`)

## Error Codes

Error codes follow the pattern: `E-<DOMAIN>-<NUMBER>`
- **DOMAIN** abbreviations: CHK (Checkout), ORD (Ordering), PAY (Payment), VCH (Voucher), BSK (Basket), COM (Communications), CON (Consumer)
- **NUMBER**: Zero-padded 4-digit sequential number
- Document error codes in appropriate `errorCodes<Domain>.md` files
- Include error code name and detailed description

## Code Review Requirements

Before submitting changes:
1. Verify YAML syntax is valid (no tabs, correct indentation)
2. Ensure all problem URLs follow the standard format
3. Check that JSON examples are valid and properly formatted
4. Confirm markdown formatting renders correctly
5. Validate that both `.md` and `.yaml` files are consistent
6. Ensure error codes are unique and follow naming convention

## Content Guidelines

- Write clear, concise descriptions that help API consumers understand the error
- Include realistic examples that reflect actual API usage
- Be specific about when each error occurs
- Document any conditional or mutually exclusive fields
- Maintain a professional, technical tone
- Avoid internal implementation details

## Build and Test

This repository is a static documentation site with no build process. Changes can be validated by:
1. Opening `index.html` locally in a browser
2. Checking that markdown renders correctly
3. Verifying YAML syntax with a YAML linter
4. Validating JSON examples with a JSON validator

## Code Ownership

All `.md`, `.yaml`, and `.yml` files are owned by `@Bunnings-Engineering/technicalwriters` (see `.github/CODEOWNERS`)
