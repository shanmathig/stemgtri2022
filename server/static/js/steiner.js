var numberOfRows; 
var numberOfColumns; 
var xStep; 
var yStep;
var positions = [];
let w = window.innerWidth;
let h = window.innerHeight;
var myPoint = new Point(1, 5)
var myNodeA = new Node(1, 5, "OR", true)
var myNodeB = new Node(4, 4, "OR", true)
var myNodeC = new Node(2, 8, "AND", false)
var myNodeD = new Node(3, 7, "OR", true)
var myNodeE = new Node(5, 9, "NOT", false)
var myNodeF = new Node(7, 5, "OR", true)
var myNodeG = new Node(8, 1, "NOT", false)
var myNodeH = new Node(10, 2, "OR", true)
var myNodeI = new Node(10, 10, "OR", true)

  
function setup(){
    createCanvas(w+5, h+5);

  numberOfColumns = 10; 
  numberOfRows = 10; 

  xStep = (w)/numberOfColumns; 
  yStep = (h)/numberOfRows; 
  for(var x = 0; x < width; x += xStep){
    for(var y = 0; y < height; y += yStep){ 
      var p = createVector(x, y);
      positions.push(p);
    }
    
  }
 
}

function draw(){
  
  fill(250, 100, 100);

  for(var i = 0; i < positions.length; i++){ 
    ellipse(positions[i].x, positions[i].y, 5, 5);
  }

myNodeA.createGrid();
myNodeB.createGrid();
myNodeC.createGrid();
myNodeD.createGrid();
myNodeE.createGrid();
myNodeF.createGrid();
myNodeG.createGrid();
myNodeH.createGrid();
myNodeI.createGrid();
}

