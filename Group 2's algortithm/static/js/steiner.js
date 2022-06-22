var numberOfRows; 
var numberOfColumns; 
var xStep; 
var yStep;
var positions = [];
let w = window.innerWidth;
let h = window.innerHeight

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
  
stroke("black")
  for(var i = 0; i < positions.length; i++){ 
    ellipse(positions[i].x, positions[i].y, 5, 5);
  }

var nodeinit = nodelistinit[0];
// var nodefinal = nodelistfinal[0];
// for (var i = 0; i< nodefinal.length; i++){
//   fill('black');
//   ellipse((w/10)*nodefinal[i][0], h-(h/10)*nodefinal[i][1], 20, 20);
// }
for (var i = 0; i< nodeinit.length; i++){
  fill('red');
  ellipse(xStep*nodeinit[i][0], h-(yStep*nodeinit[i][1]), 20, 20);
} 
fill("black");
text(nodeinit, 50, 50);
var msti2 = msti[0]
var x = 50;
var y = 50;
stroke("black")
for(var i = 0; i < nodeinit.length; i++){
  console.log("hello")
  line(xStep*nodeinit[i][0], 0, xStep*nodeinit[i][0], h)
  line(0,h-(yStep*nodeinit[i][1]), w,h-(yStep*nodeinit[i][1]))

}
sleep(5000).then(() => { console.log("World!"); });
stroke("red")
for (var i = 0; i< msti2.length; i++){
  mstilines = line(xStep*nodeinit[msti2[i][0]][0], h-(yStep*nodeinit[msti2[i][0]][1]), xStep*nodeinit[msti2[i][1]][0], h-(yStep*nodeinit[msti2[i][1]][1]))
  
} 
mstilines.show()
text(msti2, 70, 50);

}



