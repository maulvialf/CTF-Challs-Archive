const createDOMPurify = require('dompurify');
const { JSDOM }       = require('jsdom');

const filterHTML = (userHTML) => {
    window = new JSDOM('').window;
    DOMPurify = createDOMPurify(window);
    return DOMPurify.sanitize(userHTML, {
        ALLOWED_TAGS: ['strong', 'em', 'b', 'img', 'a', 's', 'ul', 'ol', 'li']
    });
}

const filterMeta = (metaHTML) => {
    window = new JSDOM('').window;
    DOMPurify = createDOMPurify(window);
    sanitized = DOMPurify.sanitize(metaHTML, {
        ALLOWED_TAGS: ['meta'],
        ALLOWED_ATTR: ['name', 'content', 'property', 'http-equiv'],
        WHOLE_DOCUMENT: true
    });
    return new JSDOM(sanitized).window.document.head.innerHTML;
}

const generateMeta = (title, description, keywords) => {
    return filterMeta(
    `
        <meta http-equiv="Content-Security-Policy" content="script-src 'self' 'unsafe-inline'">
        <meta property="og:title" content="${title}" />
        <meta property="og:description" content="${description}" />
        <meta name="keywords" content="${keywords}" />
    `);
}

module.exports = {
    filterMeta,
	filterHTML,
    generateMeta
};