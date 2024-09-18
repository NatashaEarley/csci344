
const changeBg = (sel, color) => {
    document.querySelector(sel).style.backgroundColor = color;
};

const clearBgs = () => {
    const divs = document.querySelectorAll('.my-section');
    for (const div of divs) {
        div.style.backgroundColor = 'transparent';
    }
}