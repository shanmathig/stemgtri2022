var numberOfRows; 
var numberOfColumns; 
var xStep; 
var yStep;
var positions = [];
let w = window.innerWidth;
let h = window.innerHeight
var k = 0;

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

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function draw(){

  fill(250, 100, 100);
  fill(255,0,0);

  var nodeinit = nodelistinit[0];
  var nodefinal = nodelistfinal;
//FUNCTIONS START HERE
//Grid Points  
function gridpts(){
stroke("black")
  for(var i = 0; i < positions.length; i++){ 
    ellipse(positions[i].x, positions[i].y, 5, 5);
  }
}
//Initial MST Nodes
function initnodes(){
for (var i = 0; i< nodeinit.length; i++){
  fill('red');
  ellipse(xStep*nodeinit[i][0], h-(yStep*nodeinit[i][1]), 20, 20);
} 
}

//Initial MST Lines
function initlines(){
var msti2 = msti[0]
  stroke("red")
  strokeWeight(1)
  for (var i = 0; i< msti2.length; i++){
    line(xStep*nodeinit[msti2[i][0]][0], h-(yStep*nodeinit[msti2[i][0]][1]), xStep*nodeinit[msti2[i][1]][0], h-(yStep*nodeinit[msti2[i][1]][1]))
  } 
}
//Underlying Grid Graph
function grid(){
    stroke("black")
    strokeWeight(0.5)
    for(var i = 0; i < nodeinit.length; i++){
      line(xStep*nodeinit[i][0], 0, xStep*nodeinit[i][0], h)
      line(0,h-(yStep*nodeinit[i][1]), w,h-(yStep*nodeinit[i][1]))
    }
}

//Re-display initial MST and grid 
function redisplayMST(){
    gridpts();
    initnodes();
    initlines();
    grid();  

}
//Re-displays just initial grid
function redisplay(){
    gridpts();
    grid();  
 }
//FUNCTIONS END HERE

//1.) Introduction: Initial MST
gridpts()
sleep(2000)
  .then(() => initnodes())
  .then(() => sleep(2000))
  .then(() => initlines())
  .then(() => sleep(2000))
  .then(() => grid())
  .then(() => sleep(2000))
  .then(() => iterate())
  .then(() => sleep(2000))

//2.) Intermediate MSTs
function iterate(){
 for(var k= 0; k < nodefinal.length; k++){
    for(var j = 0; j< nodefinal[k].length; j++){
      //Display Each Addition of Node 
      fill("blue");
       var point = nodefinal[k][j]
       var pointX = point[0]
       var pointY = point[1]
       
       ellipse(xStep*pointX, h-(yStep*pointY), 10, 10);
       //Display Each Addition of Wire
       stroke("blue")
       strokeWeight(1)
       let msts2 = msts[k]
       for(var p = 0; p< msts2.length; p++){
       var point1 = msts2[p][0] //(0) -> 9
       var point2 = msts2[p][1] //(9) -> 1
       coordinate1 = nodefinal[k][point1] //nodefinal[0][0] : 1,5 -> 4,5
       coordinate2 = nodefinal[k][point2] //nodefinal[0][9] : 4,5 -> 4,4
       line(xStep*coordinate1[0], h-(yStep*coordinate1[1]), xStep*coordinate2[0], h-(yStep*coordinate2[1]))
      }
    }
  }
 // }
 console.log(k)
   //Pause to differentiate between each iteration 
   //????   
  

noLoop();

}

}