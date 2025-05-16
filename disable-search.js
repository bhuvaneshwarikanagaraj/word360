// Disable text selection
document.addEventListener('selectstart', function(e) {
    e.preventDefault();
    return false;
});

// Disable right-click context menu
document.addEventListener('contextmenu', function(e) {
    e.preventDefault();
    return false;
});

// Disable copy
document.addEventListener('copy', function(e) {
    e.preventDefault();
    return false;
});

// Disable cut
document.addEventListener('cut', function(e) {
    e.preventDefault();
    return false;
});

// Disable paste
document.addEventListener('paste', function(e) {
    e.preventDefault();
    return false;
});

// Add CSS to disable text selection
const style = document.createElement('style');
style.textContent = `
    * {
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
    }
    
    /* Allow selection in input fields and textareas */
    input[type="text"],
    input[type="password"],
    input[type="email"],
    input[type="number"],
    input[type="tel"],
    input[type="url"],
    textarea {
        -webkit-user-select: text;
        -moz-user-select: text;
        -ms-user-select: text;
        user-select: text;
    }
`;
document.head.appendChild(style); 