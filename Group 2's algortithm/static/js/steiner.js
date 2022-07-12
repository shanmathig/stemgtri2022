var numberOfRows; 
var numberOfColumns; 
var xStep; 
var yStep;
var positions = [];
let w = window.innerWidth/2;
let h = w
var k = 0;

function setup(){

  createCanvas(w+10, h+10);
  stroke(2)
  line(0, 0, 0, w)
 
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
  clear()
    gridpts();
    grid();  
 }
//FUNCTIONS END HERE

//1.) Introduction: Initial MST
gridpts()
sleep(2000)
  .then(() => initnodes())
  .then(() => sleep(3000))
  .then(() => initlines())
  .then(() => sleep(3000))
  .then(() => grid())
  .then(() => sleep(3000))
  .then(() => iterate(0))
  .then(() => sleep(3000))
  .then(() => iterate(1))
  .then(() => sleep(3000))
  .then(() => iterate(2))
  .then(() => sleep(3000))
  .then(() => iterate(3))

console.log(nodeinit)
console.log(nodefinal)
console.log(msts.length)
console.log(nodeinit)
console.log(msts[0])
console.log(msts[1])
console.log(msts[2])
console.log(msts[3])

nodeCombined = nodeinit.concat(nodefinal[0])

//2.) Intermediate MSTs
function iterate(k){
// for(var k= 0; k < msts.length; k++){
    for(var j = 0; j< msts[k].length; j++){
      //Display Each Addition of Node 
      msts2 = msts[k]
      redisplay()
       for (var i = 0; i< msts2.length+1; i++){
        fill('blue');
        ellipse(xStep*nodeCombined[i][0], h-(yStep*nodeCombined[i][1]), 20, 20);
      } 
       //Display Each Addition of Wire
       stroke("blue")
       strokeWeight(1)
       console.log(msts[0])
       console.log(msts[1])
console.log(nodeCombined)
       for(var p = 0; p< msts2.length; p++){
          point1 = msts2[p][0] //(0) 
          point2 = msts2[p][1] //(9)

          coordinate1 = nodeCombined[point1] //nodeinit[0][0] : 1,5 -> 4,5
          coordinate2 = nodeCombined[point2] //nodeinit[0][9] : 4,5 -> 4,4
         console.log(coordinate1)
         console.log(coordinate2)
         
         console.log(point1)
         console.log(point2)
 
          line(xStep*coordinate1[0], h-(yStep*coordinate1[1]), xStep*coordinate2[0], h-(yStep*coordinate2[1]))

      }

    
  }
 // }
   //Pause to differentiate between each iteration 
   //????   


}
noLoop();


}