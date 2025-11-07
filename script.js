/**
 * @file Manages dynamic content loading, XSLT transformation, and search functionality for the API problems page.
 */

/**
 * Handles URL parameters to determine which markdown document to display.
 * Only loads content into docContainer when viewing a specific problem type or error code page.
 * When on the main page (no parameters), docContainer remains empty to avoid duplication
 * since index.md is loaded separately into indexHeading.
 */
var urlParams = new URLSearchParams(location.search);
var docContainer = document.getElementById('docContainer');
if (urlParams.has('type')) {
    var doc = "./" + urlParams.get('type') + ".md";
    docContainer.innerHTML = "<zero-md src='" + doc + "'></zero-md>";
} else if (urlParams.has('codes')) {
    var doc = "./" + urlParams.get('codes') + ".md";
    docContainer.innerHTML = "<zero-md src='" + doc + "'></zero-md>";
}

/**
 * Search state management
 */
let searchData = {
    problems: [],
    errorCodes: []
};

/**
 * Initialize search functionality
 */
function initializeSearch() {
    const searchInput = document.getElementById('searchInput');
    const clearButton = document.getElementById('clearSearch');
    
    if (!searchInput) return;
    
    // Load search data
    loadSearchData();
    
    // Search input handler with debounce
    let searchTimeout;
    searchInput.addEventListener('input', function(e) {
        const query = e.target.value.trim();
        
        // Show/hide clear button
        if (query) {
            clearButton.style.display = 'block';
        } else {
            clearButton.style.display = 'none';
        }
        
        // Debounce search
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
            performSearch(query);
        }, 300);
    });
    
    // Clear button handler
    clearButton.addEventListener('click', function() {
        searchInput.value = '';
        clearButton.style.display = 'none';
        performSearch('');
        searchInput.focus();
    });
    
    // Clear on Escape key
    searchInput.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            searchInput.value = '';
            clearButton.style.display = 'none';
            performSearch('');
        }
    });
}

/**
 * Load search data from the index files
 */
async function loadSearchData() {
    try {
        // Load problem types from index.xml
        const indexResponse = await fetch('./index.xml');
        const indexText = await indexResponse.text();
        const parser = new DOMParser();
        const indexDoc = parser.parseFromString(indexText, "application/xml");
        const problems = indexDoc.querySelectorAll('problem');
        
        searchData.problems = Array.from(problems).map(problem => ({
            title: problem.getAttribute('title'),
            href: problem.getAttribute('href'),
            type: 'problem'
        }));
        
        // Load error code domains from errorCodes.xml
        const errorCodesResponse = await fetch('./errorCodes.xml');
        const errorCodesText = await errorCodesResponse.text();
        const errorCodesDoc = parser.parseFromString(errorCodesText, "application/xml");
        const errorCodes = errorCodesDoc.querySelectorAll('problem');
        
        searchData.errorCodes = Array.from(errorCodes).map(code => ({
            title: code.getAttribute('title'),
            href: code.getAttribute('href'),
            type: 'errorCode'
        }));
    } catch (error) {
        console.error('Error loading search data:', error);
    }
}

/**
 * Perform search and filter visible items
 */
function performSearch(query) {
    const normalizedQuery = query.toLowerCase();
    
    // Only perform search on main page
    if (!urlParams.has('type') && !urlParams.has('codes')) {
        const indexList = document.querySelector('#index ul');
        const errorCodesList = document.querySelector('#errorCodes ul');
        
        if (indexList) {
            filterList(indexList, normalizedQuery);
        }
        
        if (errorCodesList) {
            filterList(errorCodesList, normalizedQuery);
        }
        
        // Show/hide sections if all items are hidden
        updateSectionVisibility();
    }
}

/**
 * Filter list items based on search query
 */
function filterList(list, query) {
    const items = list.querySelectorAll('li');
    let visibleCount = 0;
    
    items.forEach(item => {
        const text = item.textContent.toLowerCase();
        const link = item.querySelector('a');
        
        if (!query || text.includes(query)) {
            item.classList.remove('search-hidden');
            visibleCount++;
            
            // Highlight matching text
            if (query && link) {
                highlightText(link, query);
            } else if (link) {
                // Remove highlights if no query
                const originalText = link.getAttribute('data-original-text');
                if (originalText) {
                    link.textContent = originalText;
                }
            }
        } else {
            item.classList.add('search-hidden');
        }
    });
    
    return visibleCount;
}

/**
 * Highlight matching text in element
 */
function highlightText(element, query) {
    const originalText = element.getAttribute('data-original-text') || element.textContent;
    if (!element.hasAttribute('data-original-text')) {
        element.setAttribute('data-original-text', originalText);
    }
    
    if (!query) {
        element.textContent = originalText;
        return;
    }
    
    const regex = new RegExp(`(${escapeRegex(query)})`, 'gi');
    const highlightedText = originalText.replace(regex, '<span class="search-highlight">$1</span>');
    element.innerHTML = highlightedText;
}

/**
 * Escape special regex characters
 */
function escapeRegex(str) {
    return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

/**
 * Update section visibility based on search results
 */
function updateSectionVisibility() {
    const indexSection = document.querySelector('.content-section:first-child');
    const errorCodesSection = document.querySelector('.error-codes-section');
    
    if (indexSection) {
        const indexList = document.querySelector('#index ul');
        const visibleItems = indexList ? indexList.querySelectorAll('li:not(.search-hidden)').length : 0;
        
        if (visibleItems === 0 && indexList) {
            const existingNoResults = indexSection.querySelector('.search-no-results');
            if (!existingNoResults) {
                const noResults = document.createElement('div');
                noResults.className = 'search-no-results';
                noResults.innerHTML = '<p>No problem types match your search.</p>';
                indexSection.appendChild(noResults);
            }
        } else {
            const noResults = indexSection.querySelector('.search-no-results');
            if (noResults) noResults.remove();
        }
    }
    
    if (errorCodesSection) {
        const errorCodesList = document.querySelector('#errorCodes ul');
        const visibleItems = errorCodesList ? errorCodesList.querySelectorAll('li:not(.search-hidden)').length : 0;
        
        if (visibleItems === 0 && errorCodesList) {
            const existingNoResults = errorCodesSection.querySelector('.search-no-results');
            if (!existingNoResults) {
                const noResults = document.createElement('div');
                noResults.className = 'search-no-results';
                noResults.innerHTML = '<p>No error code domains match your search.</p>';
                errorCodesSection.appendChild(noResults);
            }
        } else {
            const noResults = errorCodesSection.querySelector('.search-no-results');
            if (noResults) noResults.remove();
        }
    }
}

/**
 * Update active nav link based on current page
 */
function updateActiveNavLink() {
    const navLinks = document.querySelectorAll('.nav-link');
    const currentPath = window.location.search;
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        const linkPath = new URL(link.href).search;
        
        if ((!currentPath && linkPath === '') || (currentPath && linkPath === currentPath)) {
            link.classList.add('active');
        }
    });
}

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
 * and loads 'index.md' and 'errorCodes.md' for the headings.
 */
if (!urlParams.has('type') && !urlParams.has('codes')) {
    // Load the heading and introduction from index.md
    document.getElementById('indexHeading').innerHTML = "<zero-md src='index.md'></zero-md>";
    // Load the problem types list
    loadAndTransformXml('./index.xml', './index.xsl', 'index');
    
    // Load the error codes heading from errorCodes.md
    document.getElementById('errorCodesHeading').innerHTML = "<zero-md src='errorCodes.md'></zero-md>";
    // Load the error codes list
    loadAndTransformXml('./errorCodes.xml', './index.xsl', 'errorCodes');
    
    // Show the main page content
    document.getElementById('mainPageContent').style.display = 'block';
} else {
    // Hide the main page content when viewing specific problem or error code
    document.getElementById('mainPageContent').style.display = 'none';
}

// Initialize search functionality when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    initializeSearch();
    updateActiveNavLink();
    
    // Re-initialize search after content is loaded
    setTimeout(() => {
        initializeSearch();
    }, 1000);
});
