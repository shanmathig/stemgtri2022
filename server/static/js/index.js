let w = window.innerWidth;
let h = window.innerHeight;

function setup() {
    var canvas = createCanvas(w, h);
}

function draw() {
    background(255, 255, 255);
    circle(50, 50, 20)
}

//window resize done
function windowResized() {
    resizeCanvas(windowWidth, windowHeight);
    let w = window.innerWidth;
    let h = window.innerHeight;
}