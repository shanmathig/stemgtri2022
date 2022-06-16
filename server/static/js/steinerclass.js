class Fun{
    constructor(x, y, r){
        this.x = x;
        this.y = y;
        this.r= r;
    }
    drawCircle(x, y, r){
        fill(255, 0, 0);
        circle(x,y,r);
    }


}

class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }

    drawPoint(strokeWeight, strokeColor, coordinateGridReference, type) {
        if (strokeColor === undefined) {
            strokeColor = 'black';
        }
        if (type !== undefined) {
            noStroke();
            text(type, this.x + 30, this.y + 20);
        }
        stroke(strokeColor).strokeWeight(strokeWeight);
        circle(this.x, this.y, 40);
        stroke('black');
    }
}

class Node extends Point {
    constructor(x, y, type, isRoot) {
      super(x, y) 
      this.type = type;
      this.isRoot = isRoot;
      this.edges = [];
      
    }
    drawPoint() {
        var drawColor;
      if (this.type == "AND"){
        drawColor = 'orange';
      }
      else if(this.type == "OR"){
        drawColor = 'blue';
      }
      else if(this.type == "NOT"){
        drawColor = 'green';
      }
      else if (this.isRoot){
        drawColor = "red"
      }
      super.drawPoint(20, drawColor, undefined, this.type);

      }

    }
  

//Now for the whole thing!