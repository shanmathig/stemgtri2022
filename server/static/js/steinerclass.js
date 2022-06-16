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

    drawPoint(strokeWeight, fillColor, coordinateGridReference, type) {
        if (fillColor === undefined) {
            fillColor = 'black';
        }
        if (type !== undefined) {
            noFill();
            text(type, this.x + 30, this.y + 20);
        }
        fill(fillColor);
        ellipse(this.x, this.y, 20, 20);
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

class Grid {
    constructor(windowWidth, windowHeight, numColumns, numRows) {
        this.windowWidth = windowWidth;
        this.windowHeight = windowHeight;
        this.numColumns = numColumns;
        this.numRows = numRows;
        
        this.nodePoints = {};
        this.points = [];
    }
    drawPoints() {
        for (var i = 0; i < this.points.length; i++) {
            for (var j = 0; j < this.points[i].length; j++) {
                var pointObject = this.points[i][j];
                pointObject.drawPoint(5, undefined, this);
            }   
        }
    }
    
    getIdAndLabel(node) {
        var id = node.substring(node.lastIndexOf("<") + 1, node.lastIndexOf(">"));
        var label = node.replace(/<.*>/, '').replace(/[.*]/, '');
        return {
            id, label
        }
    }

    getNodePoint(id) {
        return this.nodePoints[id];
    }

    addNodePoint(id, nodePoint) {
        this.nodePoints[id] = nodePoint;
    }

    loadNodePoints(nodeData) {
        for (const [key, value] of Object.entries(nodeData)) {
            var relativeX = value.coordinates[0];
            var relativeY = value.coordinates[1];
            var {realX, realY} = this.calculateRealCoords(relativeX, relativeY);
            var {id, label} = this.getIdAndLabel(key);
            var rootNodeStatus = value.root_node;

            print(this.points[relativeX][relativeY])
            var newNodePoint = new NodePoint(
                relativeX, // relativeX
                relativeY, // relativeY
                realX, // x
                realY, // y
                id, // id
                label, // label
                rootNodeStatus // rootNode
            );
            this.points[relativeX][relativeY] = newNodePoint;
            this.addNodePoint(id, newNodePoint);
        }
    }
}