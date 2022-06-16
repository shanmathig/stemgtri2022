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




// function setup() {
// var canvas = createCanvas(w, h);
// textSize(sizeOfText);
// textAlign(CENTER)
// strokeWeight(5)
// frameRate(60);
// // print(jsonData['data']); 
  
//   numberOfColumns = 10; 
//   numberOfRows = 10; 
  
//   xStep = 400/numberOfColumns; 
//   yStep = 400/numberOfRows; 
//   for(var x = 0; x < width; x += xStep){ 
//     for(var y = 0; y < height; y += yStep){ 
//       var p = createVector(x, y);
//       positions.push(p); 
      
//     }
// }
// }
    
// function draw() {
//   background(220);
//    fill(250, 100, 100);
   
//   for(var i = 0; i < positions.length; i++) { 
//     ellipse(positions[i].x, positions[i].y, 2, 2);   
//     }  
// }

// class Node {
//     constructor(name, x, y, logic_type) {
//         this.name = name;
//         this.x = x;
//         this.y = y;
//         this.logic_type = logic_type;
//     }

//     displayNode() {
//         if (this.logic_type == "and") {
//             fill(255, 0, 0)
//             circle(this.x*40, this.y*40, 10);
//         }
//         else if(this.logic_type == "or") {
//             fill(0, 255, 0)
//             circle(this.x*40, this.y*40, 10);
//         }
//         else {
//             fill(0, 0, 255)
//             circle(this.x*40, this.y*40, 10);
//         }

//     }
// }


// class Wire{
//     constructor(wireName, wireLength, startX, startY, endX, endY) {
//         this.wireName = wireName;
//         this.wireLength = wireLength;
//         this.startX = startX;
//         this.startY = startY;
//         this.endX = endX;
//         this.endY = endY; 
//     }
// }

  

  
  



