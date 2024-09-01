let canvasWidth = window.innerWidth;
let canvasHeight = window.innerHeight;

function setup() {
    createCanvas(canvasWidth, canvasHeight);
    draw5CirclesFor ();
    draw5CirclesWhile();
    drawNCircles(7);
    drawNCirclesFlexible(20, 40, 400, 0);
    drawNShapesFlexible(10, 50, 500, 0, "square");
    drawNShapesDirectionFlexible(10, 50, 600, 0, "circle", "row");
    drawGrid(canvasWidth, canvasHeight);
}

function draw5CirclesWhile () {
    noFill();

    let i = 0;
    let y = 200;
    const spacing = 50;

   while (i < 5) {
    circle(100, y, 50); 
    y += spacing;
    i++;
   }
}

function draw5CirclesFor() {
    let y = 200;
    const spacing = 50;
    for (let i = 0; i < 5; i++) {
        circle(200, y, 50);
        y += spacing;
    }
}

function drawNCircles (n) {
    let y = 200;
    const spacing = 50;
    for (let i = 0; i < n; i++) {
        circle(300, y, 50);
        y += spacing;
    }
}

function drawNCirclesFlexible(n, size, x, y) {
    for (let i = 0; i < n; i++) {
        circle(x, y, size);
        y += size;
    }
}

function drawNShapesFlexible(n, size, x, y, shape) {
    for (let i = 0; i < n; i++) {
        if (shape === "circle") {
                circle(x, y, size);
        } else {
                square(x, y, size);
        }
        y += size;
    }
}

function drawNShapesDirectionFlexible(n, size, x, y, shape, direction) {
    for (let i = 0; i < n; i++) {
        if (shape === "circle") {
            circle(x, y, size);
        } else {
            square(x, y, size);
        }

        if (direction === "row") {
            x += size;
        } else {
            y += size;
        }
    }
}

// I referenced W3schools and used ChatGPT to relearn some of the structures for the functions