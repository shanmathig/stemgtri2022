class CoordinateGrid {
    constructor(windowWidth, windowHeight, numColumns, numRows) {
        this.points = [];
        this.windowWidth = windowWidth;
        this.windowHeight = windowHeight;
        this.numColumns = numColumns;
        this.numRows = numRows;
        this.nodePoints = {};
        for (var i = 0; i <= this.numColumns; i++) {
            this.points[i] = [];
            for (var j = 0; j <= this.numRows; j++) {
                var {realX, realY} = this.calculateRealCoords(i, j);
                this.points[i][j] = new CoordinatePoint(i, j, realX, realY);
            }
        }
    }

    drawPoints() {
        for (var i = 0; i < this.points.length; i++) {
            for (var j = 0; j < this.points[i].length; j++) {
                var pointObject = this.points[i][j];
                pointObject.drawPoint(5, undefined, this);
            }   
        }
    }

    calculateRealCoords(relativeX, relativeY) {
        var realX = relativeX * ((this.windowWidth - 2*this.windowWidth/8) / this.numColumns) + this.windowWidth/8;
        var realY = relativeY * ((this.windowHeight - 2*this.windowHeight/8) / this.numRows) + this.windowHeight/8;
        return {
            realX, realY
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