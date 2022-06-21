// classes for nodes
class Nodes {
    // initializes variables
    constructor() {
        this.nodes = {};
        this.weightColors = {};
    }

    // adds a node
    addNode(id, node){
        this.nodes[id] = node
    }

    // gets a node by id
    findNode(id){
        return this.nodes[id]
    }

    swapNodes(node_1_id, node_2_id, percent_done){
        this.updateSwapVector(node_1_id, node_2_id, percent_done)
        this.updateSwapVector(node_2_id, node_1_id, percent_done)
    }

    /*
        Algorithm = (V2-V1)*(timePassed/totalTime)+V1 (this will help with 3rd modeling if implemented)
    */
    updateSwapVector(node_1_id, node_2_id, percent_done, isRight){
        var node_1 = this.findNode(node_1_id)
        var node_2 = this.findNode(node_2_id)
        var v1, v2, v3

        v1 = createVector(node_1.x.initialX, node_1.y.initialY) // left
        v2 = createVector(node_2.x.initialX, node_2.y.initialY) // right
        if(percent_done <= .5){
            v3 = (v2.sub(v1)).mult(2*percent_done).add(v1)
        }else{
            v3 = (v1.sub(v2)).mult(2*(percent_done-.5)).add(v2)
        }
        node_1.updateX(v3.x)
        node_1.updateY(v3.y)
    }

    swapInitial(node_1_id, node_2_id){
        var node_1 = this.findNode(node_1_id)
        var node_2 = this.findNode(node_2_id)

        var coords_1 = node_1.getInitial()
        var coords_2 = node_2.getInitial()

        // x
        node_1.x.initialX = coords_2[0]
        node_2.x.initialX = coords_1[0]

        // y
        node_1.y.initialY = coords_2[1]
        node_2.y.initialY = coords_1[1]
    }

    updateNodeInitial(id){
        var node = this.findNode(id)
        node.updateX(node.x.initialX)
        node.updateY(node.y.initialY)
    }

    resize(factorX, factorY){
        for (const [id, node] of Object.entries(nodes.nodes)) {
            node.x.initialX *= factorX
            node.x.currentX *= factorX
            node.y.initialY *= factorY
            node.y.currentY *= factorY
        }
    }

    // adds a random weight color entry if it the specified edge weight does not already have one
    addWeightColor(edgeWeight) {
        if(!this.weightColors.hasOwnProperty(edgeWeight)){ //if the weight isn't recorded
            this.weightColors[edgeWeight] = color(`rgba(${Math.floor(random(255))}, ${Math.floor(random(255))}, ${Math.floor(random(255))}, 0.25)`); //weight is assigned random color
        }
    }

    // sets x and y to be used for KL based on the final x and y vals when mincut finished
    setKLXAndY(leftNodeKeys, rightNodeKeys) {
        for (const [id, node] of Object.entries(this.nodes)) {
            node.x.initialX = node.targetX;
            node.x.currentX = node.targetX;
            node.y.initialY = node.targetY;
            node.y.currentY = node.targetY;
            // locks nodes if they arent part of the KL process
            if (!leftNodeKeys.includes(id) && !rightNodeKeys.includes(id)) {
                node.locked = true;
            }
        }
    }

    // sets mincut x and y vals to be the same as the initial values it had
    updateMincutPositions(originalLeftNodeKeys, originalRightNodeKeys) {
        for (const [id, node] of Object.entries(this.nodes)) {
            if (originalLeftNodeKeys.includes(id) || originalRightNodeKeys.includes(id)) {
                node.mincutX = node.x.initialX
                node.mincutY = node.y.initialY
            }
        }
    }

    // tracks whether mincut is currently happening
    setMincutProcess(booleanVal) {
        this.mincutProcess = booleanVal;
    }

    // unlocks nodes
    unlockAllNodes() {
        for (const [id, node] of Object.entries(this.nodes)) {
            node.locked = false;
        }
    }

    // draws each node
    drawAllNodes() {
        for (const [id, node] of Object.entries(this.nodes))  {
            node.drawNodes(this.mincutProcess);
        }
    }

    // draws each edge, updates node positions, tracks if mincut is done by tracking if the nodes reached their target location
    drawAllEdges(checkCompletionOfMincut) {

        this.mincutDone = true;

        for (const [id, node] of Object.entries(this.nodes)) {
            node.drawEdges(this.mincutProcess, this.weightColors, this);

            if (this.mincutProcess) {
                node.updatePosition();
            }
            if (this.mincutProcess && checkCompletionOfMincut && node.reachedTarget() == false) {
                this.mincutDone = false;
            }
        }
        
    }

    // gets whether mincut is in process
    getMincutStatus() {
        return this.mincutDone;
    }
}

class Node {
    // initializes variables each node uses
    constructor(x, y, edges, label, locked, mincutX, mincutY, id) {
        this.x = x;
        this.y = y;
        if (edges != null) {
            this.edges = []; //keeping this list for now because looping through it one by one will happen either way (javascript object vs. array/list)
            for (var i = 0; i < edges.length; i++){
                this.edges.push(new Edge(
                    edges[i][0], // id
                    edges[i][1] // weight
                ))
            }
        }
        
        this.label = label;
        this.locked = locked;

        // only sets these variables if they're passed in as parameters when the class is initialized
        // this means they can be ignored if not needed
        if (mincutX != undefined) {
            this.mincutX = mincutX;
            this.mincutY = mincutY;
            this.id = id;
        }
    }

    updateX(x){
        this.x.currentX = x
    }

    updateY(y){
        this.y.currentY = y
    }

    getInitial(){
        return [this.x.initialX, this.y.initialY]
    }

    // draws a node
    drawNodes(mincutProcess) {
        if (mincutProcess) {
            // x and y in mincut
            var x = this.mincutX
            var y =  this.mincutY
        } else {
            // no mincut
            var x = this.x.currentX
            var y = this.y.currentY
        }
        
        // white node with alpha of .75
        fill('rgba(255,255,255,0.75)');
        
        // adds green border
        if(this.locked){
            stroke(0,255,0)
            circle(x, y, sizeOfCircle)
            stroke(0,0,0)
        }else{
            // black border around circle
            stroke(0,0,0)
            circle(x, y, sizeOfCircle)   
        }

        // displays label
        noStroke()
        fill(0,0,0)
        text(this.label, x, y+sizeOfText/4)
    }

    // draws all target edges of a source node
    drawEdges(mincutProcess, weightColorsReference, allNodes) {
        if (mincutProcess) {
            // in mincut
            var x1 = this.mincutX
            var y1 = this.mincutY
        } else {
            // x and y with no mincut
            var x1 = this.x.currentX
            var y1 = this.y.currentY
        }

        // loops through all edges a node connects to
        this.edges.forEach((edge) => {
            var otherNode = allNodes.findNode(edge.id);
            if (mincutProcess) {
                // gets x and y of edge node in mincut
                var x2 = otherNode.mincutX;
                var y2 = otherNode.mincutY;
            } else {
                // gets x and y of edge node with no mincut
                var x2 = otherNode.x.currentX;
                var y2 = otherNode.y.currentY;
            }

            // draws the edge
            stroke(weightColorsReference[edge.weight])
            line(x1, y1, x2, y2)
        })
    }

    // checks whether node has reached the target specified by mincut
    reachedTarget() {
        return (this.mincutX <= this.targetX + 10 && this.mincutX >= this.targetX - 10) && (this.mincutY <= this.targetY + 10 && this.mincutY >= this.targetY - 10)
    }

    // moves x and y positions closer to the target of mincut so that the nodes are within a quadrant
    // moves them so that they are only within 10px of the actual location they should be in
    // this causes the transition between mincut and KL to be a bit jumpy
    updatePosition() {
        if (this.mincutX > this.targetX + 10) {
            this.mincutX -= 10;
        } else if (this.mincutX < this.targetX - 10) {
            this.mincutX += 10;
        }

        if (this.mincutY > this.targetY + 10) {
            this.mincutY -= 10;
        } else if (this.mincutY < this.targetY - 10) {
            this.mincutY += 10;
        }
    }

}

class Edge {
    // stores id and weight of an edge
    constructor(id, weight) {
        this.id = id;
        this.weight = weight;
    }
}


// loads KL data
class Data {
    constructor(data){
        this.iterations = []
        for(var i = 1; i < data.length; i++){
            if(typeof data[i]["gain"] == 'undefined'){
                this.iterations.push(new Iteration(
                    data[i]["cutsize"], // cutsize
                    null, // gain
                    null, // pair
                    null // swap_time
                ))
            }else{
                this.iterations.push(new Iteration(
                    data[i]["cutsize"], // cutsize
                    data[i]["gain"], // gain
                    data[i]["pair"], // pair
                    data[i]["swap_time"] // swap_time
                ))
            }
        }
    }

    getIteration(index){
        return this.iterations[index]
    }
}

// loads KL iteration
class Iteration {
    constructor(cutsize, gain, pair, swap_time){
        this.cutsize = cutsize
        this.gain = gain
        this.pair = pair
        this.swap_time = swap_time
    }
}

// loads mincut data
class MincutCutData {
    constructor(json) {
        //Object.assign(json, this);
        this.iterationData = [];
        this.extractIterationData(json);
        this.sortByCoords();
    }

    // creates objects based on json data
    extractIterationData(json) {
        for (var i = 1; i < json.length; i++) {
            var currentJSONData = json[i];
            if (this.iterationData[currentJSONData['cut_number']] == undefined) {
                this.iterationData[currentJSONData['cut_number']] = [];
            }
            this.iterationData[currentJSONData['cut_number']].push(new MincutIteration(
                currentJSONData['cut_direction'], // cut_direction
                currentJSONData['cut_number'], // cut_number
                currentJSONData['group_1_coords'], // group_1_coords
                currentJSONData['group_2_coords'], // group_2_coords
                currentJSONData['group_1_nodes'], // group_1_nodes
                currentJSONData['group_2_nodes'], // group_2_nodes
                currentJSONData['KL_sequence'] // KL_sequence
            ));
        }
    }

    // calculates how many quadrants there are in a specified mincut cut depth
    getNumQuadrantsInIterDepth(iterationDepth) {
        return (this.iterationData[iterationDepth].length * 2)
    }

    // calculate how to set the gridX and gridY of a new quadrant based on how many quadrants are to the left or right
    calculateCoordinateShift(iterationDepth, cutNumber) {
        return Math.floor(this.iterationData[iterationDepth][cutNumber].group_1_nodes.length ** (1/2));
    }

    // get the gridX and gridY coords of a certain mincut cut
    getGroupCoords(iterationDepth, cutNumber, groupName) {
        let x_coord = this.iterationData[iterationDepth][cutNumber][groupName][0]
        let y_coord = this.iterationData[iterationDepth][cutNumber][groupName][1]
        return {
            x_coord, y_coord 
        }
    }

    // get which nodes are inside a quadrant
    getGroupNodes(iterationDepth, cutNumber, groupName) {
        return this.iterationData[iterationDepth][cutNumber][groupName];
    }

    // return the KL sequence data
    getKLSequence(iterationDepth, cutNumber) {
        return this.iterationData[iterationDepth][cutNumber]['KL_sequence'];
    }

    // 
    /*getIterationData() {
        return this.iterationData;
    }*/

    // the actual sorting function for mincut cutsizes
    sortCompareCoords(cut_direction) {
        return function(a, b) {
            if (cut_direction == 'V') {
                // for vertical cuts, lower x values are cut first
                return a['group_1_coords'][0] - b['group_1_coords'][0];
            } else {
                // for horizontal cuts, lower y values are cut first
                return a['group_1_coords'][1] - b['group_1_coords'][1];
            }
        }
    }

    // runs sort function for all the different mincut depths
    // this prevents mincut from happening in the wrong order (ex. the top quadrant being half shrunk, then the bottom being half shrunk, then the other half of the top)
    sortByCoords() {
        for (var i = 0; i < this.iterationData.length; i++) {
            this.iterationData[i].sort(this.sortCompareCoords(this.iterationData[i][0]['cut_direction']))
        }
    }
}

// stores data for mincut iteration
class MincutIteration {
    constructor(cut_direction, cut_number, group_1_coords, group_2_coords, group_1_nodes, group_2_nodes, KL_sequence) {
        /*
        params:
            this.cut_direction
            this.cut_number,
            this.group_1_coords
            this.group_2_coords
            this.group_1_nodes
            this.group_2_nodes
            this.KL_sequence
        */
        this.cut_direction = cut_direction;
        this.cut_number = cut_number;
        this.group_1_coords = group_1_coords;
        this.group_2_coords = group_2_coords;
        this.group_1_nodes = group_1_nodes;
        this.group_2_nodes = group_2_nodes;
        this.KL_sequence = KL_sequence;
    }
}

class Quadrant {
    constructor(x, y, width, height, targetWidth, targetHeight, gridX, gridY) {
        //Object.assign(this, json);
        /* 
        params:
            this.x
            this.y
            this.width
            this.height
            this.targetHeight
            this.targetWidth
            this.gridX
            this.gridY
        also contains: 
            this.quadrantNodeArray
            this.startShrinking
            this.dividingWidth
            this.dividingHeight
        */
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.targetWidth = targetWidth;
        this.targetHeight = targetHeight;
        this.gridX = gridX;
        this.gridY = gridY;
    }
    
    // sets quadrant's target width & adjusts current width to be only slightly larger than target
    setTargetWidth(targetWidth) {
        this.targetWidth = targetWidth;
        this.width = targetWidth + 25;
        
        this.startShrinking = false;
    }

    // sets a quadrant's target height, adjusts current height to be only slightly larger than target 
    setTargetHeight(targetHeight) {
        this.targetHeight = targetHeight;
        this.height = targetHeight + 25;
        
        this.startShrinking = false;
    }

    // shrinks width of quadrant
    divideWidth() {
        if (this.width > this.targetWidth) {
            this.width -= 1;
        } else {
            if (this.dividingWidth == true) {
                this.startShrinking = false;
            }
        }
    }

    // shrinks height of quadrant
    divideHeight() {
        if (this.height > this.targetHeight) {
            this.height -= 1;
        } else {
            if (this.dividingHeight == true) {
                this.startShrinking = false;
            }
        }
    }

    // shrinks the quadrant to its required width or height and redraws it
    updateRect() {
        fill(200);
        noStroke();
        if (this.startShrinking == true) {
            this.divideHeight();
            this.divideWidth();
        }
        rect(this.x, this.y, this.width, this.height);
    }

    // specifies new targets for nodes based on which quadrant they're inside of
    updateNodePositions(nodesReference) {
        if (this.quadrantNodeArray != undefined) {

            var lengthOfQuadrantNodeArray = this.quadrantNodeArray.length;
            var xPosMultiplier = this.x;
            var yPosMultiplier = this.y;
            
            var incrementX = ((this.targetWidth) / (lengthOfQuadrantNodeArray ** (1/2)));
            var incrementY = ((this.targetHeight) / (lengthOfQuadrantNodeArray / (lengthOfQuadrantNodeArray ** (1/2))));

            xPosMultiplier += incrementX / 2;
            yPosMultiplier += incrementY / 2;

            
            for (var i = 0; i < lengthOfQuadrantNodeArray; i++) {
                var currentNodeId = this.quadrantNodeArray[i];
                var currentNodeObject = nodesReference.findNode(currentNodeId);
                
                if (i % Math.floor(lengthOfQuadrantNodeArray ** (1/2)) == 0) {
                    if (i != 0) {
                        xPosMultiplier = this.x + (incrementX / 2);
                        yPosMultiplier += incrementY / 2;

                    }
                }

                currentNodeObject.targetX = xPosMultiplier;
                currentNodeObject.targetY = yPosMultiplier;

                xPosMultiplier += incrementX;
            }
        }
    }
}

// stores all the quadrants
class QuadrantManager {
    constructor() {
        // format of this.quadrants: {0: {0: Quadrant}, 1: {0:Quadrant, 2: Quadrant}}
        this.quadrants = {}
    }

    // adds a quadrant based on its gridX and gridY position
    addQuadrant(quadrantToAdd) {
        var gridX = quadrantToAdd.gridX;
        var gridY = quadrantToAdd.gridY;
        try {
            this.quadrants[gridX][gridY] = quadrantToAdd
        } catch (e) {
            if (e instanceof TypeError) {
                try {
                    this.quadrants[gridX] = {}
                    this.quadrants[gridX][gridY] = quadrantToAdd;
                } catch (e) {
                    print(e);
                }
            }
        }
    }

    // draws all the quadrants
    drawQuadrants() {
        for (var i in this.quadrants) {
            for (var j in this.quadrants[i]) {
                var currentQuadrant = this.quadrants[i][j];
                
                currentQuadrant.updateRect();
            }
        }
    }

    // modifies which quadrant holds which nodes, updates the target positions of those nodes, allows for shrinking of quadrants/rectangles
    startShrinking(gridX, gridY, newNodesInQuadrant, nodesReference) {
        this.quadrants[gridX][gridY].quadrantNodeArray = newNodesInQuadrant;
        this.quadrants[gridX][gridY].updateNodePositions(nodesReference);
        this.quadrants[gridX][gridY].startShrinking = true;
    }

    updateAndAddQuadrants(iterationDepth, mincutReference) {
        // cutsMade tracks how many cuts have been made within an iteration depth
        var cutsMade = 0;

        // gets whether the cut is horizontal or vertical
        var cut_direction = mincutReference.iterationData[currentIter][cutsMade].cut_direction

        // loops through all quadrants and calculates their new x, y, width, and height values based on cut direction
        for (var i in this.quadrants) {
            for (var j in this.quadrants[i]) {
                var newQuadrantGridX, newQuadrantGridY;

                // for horizontal cuts
                if (cut_direction == 'H') {                    
                    // calculates new x and y position of quadrant
                    var newRectX = this.quadrants[i][j].x;
                    var newRectY = this.quadrants[i][j].y + this.quadrants[i][j].height / 2 + 5;

                    // calculates new width and height of quadrant
                    var newRectWidth = this.quadrants[i][j].width;
                    var newRectHeight = this.quadrants[i][j].height / 2 - 5;

                    // sets new gridX and gridY of quadrant
                    var newQuadrantGridX = this.quadrants[i][j].gridX
                    var newQuadrantGridY = this.quadrants[i][j].gridY + mincutReference.calculateCoordinateShift(iterationDepth, cutsMade);

                    // updates targetHeight of quadrant
                    this.quadrants[i][j].setTargetHeight(this.quadrants[i][j].height / 2 - 5);

                    
                // same as above but for vertical cuts
                } else {
                    var newRectX = this.quadrants[i][j].x + this.quadrants[i][j].width / 2 + 5;
                    var newRectY = this.quadrants[i][j].y;

                    var newRectWidth = this.quadrants[i][j].width / 2 - 5;
                    var newRectHeight = this.quadrants[i][j].height;

                    
                    var newQuadrantGridX = this.quadrants[i][j].gridX + mincutReference.calculateCoordinateShift(iterationDepth, cutsMade);
                    var newQuadrantGridY = this.quadrants[i][j].gridY

                    this.quadrants[i][j].setTargetWidth(this.quadrants[i][j].width / 2 - 5);
                }

                // overrides old quadrants and creates new ones
                var newQuadrantObject = new Quadrant(
                    newRectX, // x
                    newRectY, // y
                    newRectWidth, // width
                    newRectHeight, // height
                    newRectWidth, // targetWidth
                    newRectHeight, // targetHeight
                    newQuadrantGridX, // gridX
                    newQuadrantGridY, // gridY
                )
                // adds the quadrant
                this.addQuadrant(newQuadrantObject);
                
                // moves on to next cut within the recursion depth
                cutsMade += 1;
            }
        }
    }
}