class CoordinatePoint {
    constructor(relativeX, relativeY, x, y) {
        this.relativeX = relativeX;
        this.relativeY = relativeY;
        this.x = x;
        this.y = y;
    }

    drawPoint(strokeWeight, strokeColor, coordinateGridReference, label) {
        if (strokeColor === undefined) {
            strokeColor = 'black';
        }
        if (label !== undefined) {
            noStroke();
            text(label, this.x + 30, this.y + 20);
        }
        stroke(strokeColor).strokeWeight(strokeWeight);
        point(this.x, this.y);
        
        stroke('black');
    }
}
class NodePoint extends CoordinatePoint {
    constructor(relativeX, relativeY, x, y, id, label, rootNode) {
        super(relativeX, relativeY, x, y);
        this.id = id;
        this.label = label;
        this.rootNode = rootNode;
        this.partOfTree = rootNode;
        this.highlight = false;
        this.edges = [];
    }
    drawPoint(strokeWeight, strokeColor, coordinateGridReference) {
        this.drawEdges(coordinateGridReference);
        var drawColor;
        
        if (this.rootNode) {
            drawColor = 'orange';
        } else if (this.partOfTree) {
            drawColor = 'blue';
        } else if (this.highlight) {
            drawColor = 'green';
        } else {
            drawColor = 'red';
        }
        
        //var drawColor = (this.partOfTree) ? 'orange' : 'red';
        super.drawPoint(20, drawColor, undefined, this.label);
    }

    addToTree(boolVal) {
        this.partOfTree = boolVal;
    }

    drawEdges(coordinateGridReference) {
        for (var i = 0; i < this.edges.length; i++) {
            var edgeId = this.edges[i];

            var edgeNodeReference = coordinateGridReference.getNodePoint(edgeId);
            line(this.x, this.y, edgeNodeReference.x, edgeNodeReference.y);
        }
    }

    addEdge(edgeId) {
        this.edges.push(edgeId);
    }
}

class MSTManager {
    constructor() {
        this.MSTData = [];
        this.swapTime = (new Date()).getTime();
        this.currentIterationNumber = 0;
        this.continue = true;
    }

    loadMSTData(json) {
        for (var i = 0; i < json.length; i++) {
            var currentData = json[i];
            this.MSTData.push(new MST(
                currentData.iteration, // iteration
                currentData.T, // tree
                currentData.nearest_neighbors, // nearest_neighbors
                currentData.connection_edges, // connection_edges
                currentData.selected_connection // selected_connection
            ));
        }
    }

    addNearestNeighborHighlight(nearestNeighborsArray, add, coordinatesReference) {
        for (var i = 0; i < nearestNeighborsArray.length; i++) {
            var currentNeighbor = nearestNeighborsArray[i];
            var neighborPoint = coordinatesReference.getNodePoint(currentNeighbor);
            neighborPoint.highlight = add;
        }
    }

    completeIteration(coordinatesReference) {
        var whichSwap = timeSince(this.swapTime) / 1000;

        if (this.continue) {
            var currentNearestNeighbors = this.MSTData[this.currentIterationNumber].nearest_neighbors;
            this.addNearestNeighborHighlight(currentNearestNeighbors, true, coordinatesReference);
    
            if (Math.floor(whichSwap) > 3) {
                //console.log('test')
                var currentIterationData = this.MSTData[this.currentIterationNumber];
    
                var nodeId = currentIterationData.selected_connection[0][0];
                var edgeId = currentIterationData.selected_connection[0][1];
                var nodeObject = coordinatesReference.getNodePoint(nodeId);
                var edgeObject = coordinatesReference.getNodePoint(edgeId);
                nodeObject.addEdge(edgeId);
                nodeObject.addToTree(true);
                edgeObject.addToTree(true);
    
                this.addNearestNeighborHighlight(currentNearestNeighbors, false, coordinatesReference);
    
                this.swapTime = (new Date()).getTime();
                this.currentIterationNumber += 1;
                
            }
        }
        
        if (this.currentIterationNumber >= this.MSTData.length) {
            this.continue = false;
        }
    }
}

class MST {
    constructor(iteration, tree, nearest_neighbors, connection_edges, selected_connection) {
        this.iteration = iteration;
        this.tree = tree;
        this.nearest_neighbors = nearest_neighbors;
        this.connection_edges = connection_edges;
        this.selected_connection = selected_connection;
    }
}



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