//global variables for use throughout canvas draw
let jsonData;
let w = window.innerWidth;
let h = window.innerHeight;

const LEFT_MARGIN = w/8;
const TOP_MARGIN = h/8;
const REGULAR_POINT_SIZE = 5;
const REAL_NODE_SIZE = 20;
//const sizeOfCircle = 64;
const sizeOfText = 36;

var coordinates = new CoordinateGrid(w, h, 10, 10);
var MSTData = new MSTManager();


function preload() {
    jsonData = loadJSON('/static/algorithm_json/routing_data.json');
}

function setup() {
    var canvas = createCanvas(w, h);
    textSize(sizeOfText);
    textAlign(CENTER)
    strokeWeight(5)
    frameRate(60);
    print(jsonData['data']);


    coordinates.loadNodePoints(jsonData['data'][0]);
    MSTData.loadMSTData(jsonData['data'][1]['MST']);
}

function draw() {
    background(255, 255, 255);

    coordinates.drawPoints();
    MSTData.completeIteration(coordinates);

}