class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }

    drawPoint(strokeWeight, fillColor, coordinateGridReference, type) {
        if (fillColor === undefined) {
            fillColor = 'black';
        }
        if (type !== undefined) {
            noFill();
            text(type, this.x + 30, this.y + 20);
        }
        fill(fillColor);
        ellipse((w/10)*this.x, (h/10)*this.y, 20, 20);
        fill('black');

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
      if (this.isRoot){
            drawColor = 'red';
      }
      else if(this.type == "OR"){
        drawColor = 'blue';
      }
      else if(this.type == "NOT"){
        drawColor = 'green';
      }
      else if (this.type == "AND"){
        drawColor = "orange"
      }
      super.drawPoint(20, drawColor, undefined, this.type);
  
    }
    drawEdge() {
        for (var i = 0; i < this.edges.length; i++) {
            var edgeNodeReference = coordinateGridReference.getNodePoint(this.edges[i]); 
            line(this.x, this.y, edgeNodeReference.x, edgeNodeReference.y);
    }
}
    drawUnderlyingGrid(){
        line((w/10)*this.x, 0, (w/10)*this.x, h)
        line(0,(h/10)*this.y, w,(h/10)*this.y)
    }
    createGrid(){
        this.drawPoint();
        this.drawUnderlyingGrid();  
        

    }

}
   


//Now for the whole thing!
class CoordinateGrid {
    constructor(windowWidth, windowHeight, numColumns, numRows) {
        this.windowWidth = windowWidth;
        this.windowHeight = windowHeight;
        this.numColumns = numColumns;
        this.numRows = numRows;
        this.nodePoints = {};
        this.points = [];

        for (var i = 0; i <= this.numColumns; i++) {
            this.points[i] = [];
            for (var j = 0; j <= this.numRows; j++) {
                var {realX, realY} = this.calculateRealCoords(i, j);
                this.points[i][j] = new Point(i, j, realX, realY);
            }
        }
    }
    
}