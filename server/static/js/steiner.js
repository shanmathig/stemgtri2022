var numberOfRows; 
var numberOfColumns; 
var xStep; 
var yStep;
var positions = [];
let w = window.innerWidth;
let h = window.innerHeight;
var myFun = new Fun(100, 100, 40)
  
function setup(){
    createCanvas(w+10, h+10);

  numberOfColumns = 10; 
  numberOfRows = 10; 

  xStep = w/numberOfColumns; 
  yStep = h/numberOfRows; 
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
  myFun.drawCircle(x, y, r);

}

