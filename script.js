/**
 * @file Manages dynamic content loading and XSLT transformation for the API problems page.
 */

/**
 * Handles URL parameters to determine which markdown document to display.
 * It defaults to 'index.md' if no specific parameters are found.
 * The selected markdown document is loaded into the 'docContainer' element using the zero-md web component.
 */
var urlParams = new URLSearchParams(location.search);
var doc = "./index.md";
if (urlParams.has('type')) {
    doc = "./" + urlParams.get('type') + ".md";
}
if (urlParams.has('codes')) {
    doc = "./" + urlParams.get('codes') + ".md";
}
var docContainer = document.getElementById('docContainer');
docContainer.innerHTML = "<zero-md src='" + doc + "'></zero-md>";

/**
 * Asynchronously fetches an XML file and an XSLT file, then transforms the XML using the XSLT.
 * The resulting HTML fragment is then injected into a specified target HTML element.
 * Error handling is included for fetch failures and transformation errors.
 *
 * @async
 * @param {string} xmlPath - The path to the XML file.
 * @param {string} xsltPath - The path to the XSLT file.
 * @param {string} targetElementId - The ID of the HTML element where the transformed content will be placed.
 */
async function loadAndTransformXml(xmlPath, xsltPath, targetElementId) {
    try {
        const [xmlResponse, xsltResponse] = await Promise.all([
            fetch(xmlPath),
            fetch(xsltPath)
        ]);

        if (!xmlResponse.ok) {
            console.error(`Failed to fetch XML: ${xmlPath}`, xmlResponse.statusText);
            document.getElementById(targetElementId).innerHTML = `<p>Error loading content from ${xmlPath}</p>`;
            return;
        }
        if (!xsltResponse.ok) {
            console.error(`Failed to fetch XSLT: ${xsltPath}`, xsltResponse.statusText);
            document.getElementById(targetElementId).innerHTML = `<p>Error loading stylesheet from ${xsltPath}</p>`;
            return;
        }

        const xmlText = await xmlResponse.text();
        const xsltText = await xsltResponse.text();

        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(xmlText, "application/xml");
        const xsltDoc = parser.parseFromString(xsltText, "application/xml");

        const processor = new XSLTProcessor();
        processor.importStylesheet(xsltDoc);
        const resultDocument = processor.transformToFragment(xmlDoc, document);

        const targetElement = document.getElementById(targetElementId);
        targetElement.innerHTML = ''; // Clear previous content
        if (resultDocument) {
            // The resultDocument might be a document fragment containing a complete HTML structure (<html><body>...</body></html>)
            // from the XSLT. We want to append only the children of the body if that's the case.
            const bodyContent = resultDocument.querySelector('body');
            if (bodyContent && bodyContent.childNodes.length > 0) {
                Array.from(bodyContent.childNodes).forEach(node => targetElement.appendChild(node.cloneNode(true)));
            } else {
                targetElement.appendChild(resultDocument);
            }
        } else {
            console.error('XSLT transformation resulted in null for', xmlPath);
            targetElement.innerHTML = `<p>Error transforming content for ${xmlPath}</p>`;
        }

    } catch (error) {
        console.error('Error loading or transforming XML:', error);
        document.getElementById(targetElementId).innerHTML = `<p>An error occurred while loading content.</p>`;
    }
}

/**
 * Main logic execution block.
 * This block runs if the URL does not contain 'type' or 'codes' parameters,
 * indicating that the main index page with problem types and error codes lists should be displayed.
 * It calls `loadAndTransformXml` to populate the 'index' and 'errorCodes' divs,
 * and loads 'errorCodes.md' into the 'errorCodesHeading' div.
 */
if (!urlParams.has('type') && !urlParams.has('codes')) {
    loadAndTransformXml('./index.xml', './index.xsl', 'index');
    document.getElementById('errorCodesHeading').innerHTML = "<zero-md src='errorCodes.md'></zero-md>";
    loadAndTransformXml('./errorCodes.xml', './index.xsl', 'errorCodes');
}
