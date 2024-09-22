const defaultTheme = ev => {
    let themeChange = document.querySelector("body");
    themeChange.className = "";
};

const oceanTheme = ev => {
    let themeChange = document.querySelector("body");
    themeChange.className = "ocean";
};

const desertTheme = ev => {
    let themeChange = document.querySelector("body");
    themeChange.className = "desert";
};

const highContrastTheme = ev => {
    let themeChange = document.querySelector("body");
    themeChange.className = "high-contrast";
}; 

/*
    Hints: 
    1. Attach the event handlers (functions) above to the click event
       of each of the four buttons (#default, #ocean, #desert, 
        and #high-contrast) in index.html.
    2. Then, modify the  body of each function so that it
       sets the className property of the body tag based on 
       the button that was clicked.
*/