var numberOfRows; 
var numberOfColumns; 
var xStep; 
var yStep;
var positions = [];
let w = window.innerWidth/2;
let h = w
var k = 0;

//Setup
function setup(){
  createCanvas(window.innerWidth, window.innerHeight);
  strokeWeight(1)
  stroke("blue")

  numberOfColumns = 10; 
  numberOfRows = 10; 
  xStep = (w)/numberOfColumns; 
  yStep = (h)/numberOfRows; 

  for(var x = 0; x < w+10; x += xStep){
    for(var y = 0; y < h+10; y += yStep){ 
      var p = createVector(x, y);
      positions.push(p);
    }   
  }
}

//Sleep
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

//Draw
function draw(){
  textSize(35)
  fill('navy')
  text('Wirelength:', 850, 150)
  var nodeinit = nodelistinit[0];
  var nodefinal = nodelistfinal;

//BABY FUNCTIONS START HERE
//Grid Points  
function gridpts(){
  stroke("black")
  fill("black")
  for(var i = 0; i < positions.length; i++){ 
    ellipse(positions[i].x, positions[i].y, 5, 5);
  }
}
//Initial MST Nodes
function initnodes(){
  for (var i = 0; i< nodeinit.length; i++){
    strokeWeight(1)
    fill('red');
    ellipse(xStep*nodeinit[i][0], h-(yStep*nodeinit[i][1]), 20, 20);
} 
}
  
//Initial MST Lines
function initlines(){
  var msti2 = msti[0]
    stroke("red")
    strokeWeight(1.5)
    for (var i = 0; i< msti2.length; i++){
      line(xStep*nodeinit[msti2[i][0]][0], h-(yStep*nodeinit[msti2[i][0]][1]), xStep*nodeinit[msti2[i][1]][0], h-(yStep*nodeinit[msti2[i][1]][1]))
      textSize(50)
      text(Wirelengths[0], 910, 250)
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
function redisplayMST(p){
  if(p==true){
    clear()
    gridpts();
    initnodes();
    grid();  
    textSize(35)
    fill('navy')    
    text('Wirelength:', 850, 150)
  }
  else{
    redisplay()
  }
}

//Re-displays just initial grid
function redisplay(){
  clear()
  textSize(35)
  fill('navy')    
  text('Wirelength:', 850, 150)
  gridpts();
 }
 
//FUNCTIONS END HERE
//Intermediate MSTs
nodeCombined = nodeinit.concat(nodefinal[0])
function iterate(k, color, p, n){
  redisplayMST(p)
    for(var j = 0; j< msts[k].length; j++){
      //Display Each Addition of Node 
      msts2 = msts[k]
       for (var i = 0; i< msts2.length+1; i++){
        strokeWeight(1)
        stroke('black')
        fill(color);
        ellipse(xStep*nodeCombined[i][0], h-(yStep*nodeCombined[i][1]), n, n);
      } 
       //Display Each Addition of Wire
       stroke(color)
       strokeWeight(1.5)
       for(var p = 0; p< msts2.length; p++){
          point1 = msts2[p][0] //(0) 
          point2 = msts2[p][1] //(9)
          coordinate1 = nodeCombined[point1] //nodeinit[0][0] : 1,5 -> 4,5
          coordinate2 = nodeCombined[point2] //nodeinit[0][9] : 4,5 -> 4,4
          line(xStep*coordinate1[0], h-(yStep*coordinate1[1]), xStep*coordinate2[0], h-(yStep*coordinate2[1]))
          textSize(50)
          text(Wirelengths[k+1], 910, 250)
          console.log(Wirelengths[k])
      }
  }
}
noLoop();

//"Animation"
gridpts()
sleep(2000)
  .then(() => initnodes())
  .then(() => sleep(3000))
  .then(() => initlines())
  .then(() => sleep(3000))
  .then(() => grid())
  .then(() => sleep(3000))
  .then(() => iterate(0, 'blue', true, 13))
  .then(() => sleep(3000))
  .then(() => iterate(1, 'blue', true, 13))
  .then(() => sleep(3000))
  .then(() => iterate(2, 'blue', true, 13))
  .then(() => sleep(3000))
  .then(() => iterate(msts.length-1, 'blue', true, 16))
  .then(() => sleep(3000))
  .then(() => iterate(msts.length-1, 'green', true, 20))
  .then(() => sleep(3000))
  .then(() => clear())
  .then(() => iterate(msts.length-1, 'green', false, 20))
  .then(() => sleep(3000))

  // for(i = 0; i<msts.length; i++){
  //   if(i!=msts.length-1){
  //   sleep(2000)
  //   .then(() => iterate(i, 'blue', true, 13))
  //   }
  //   else{
  //     sleep(2000)
  //     .then(() => iterate(msts.length-1, 'blue', true, 16))
  //     .then(() => sleep(3000))
  //     .then(() => iterate(msts.length-1, 'green', true, 20))
  //     .then(() => sleep(3000))
  //     .then(() => clear())
  //     .then(() => iterate(msts.length-1, 'green', false, 20))
  //     .then(() => sleep(3000))
  //   }
  // }
}