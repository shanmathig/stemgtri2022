//global variables for use throughout canvas draw
let w = window.innerWidth
let h = window.innerHeight
let loaded = false
let isProcess = false
var maxSpeed = 10
var currentSpeed = 1
var deltaSpeed = .1
var inProcess = dateInitial()
var sizeOfCircle = 64
var sizeOfText = 36
var dataJSON
let leftNodes
let rightNodes
var currentIterationTime
var currentIteration = 0
var whichSwap;
var maxIteration
var currentCombination
var isfinished = false
var maxTimeIter = 5000
var timeIterSpeed = maxTimeIter / currentSpeed
var maxTimeIterLocked = 1000
var leftNodeKeys = []
var rightNodeKeys = []
var currentSwap = 0
var changeIteration = false
var lockedNodeTimeStart
//var weightColors = {}
var iteration_data

/*
    Classes in the 'class.js' file
*/
const nodes = new Nodes();

//functions used throughout the process
function objectSize(obj) {//returns a javascript object (dict) size
    var size = 0,
    key
    for (key in obj) {
        if (obj.hasOwnProperty(key)) size++;
    }
    return size;
};

function dateInitial(){ //returns an int of the time
    return (new Date()).getTime();
}

function timeSince(time){ //returns an int of how much time has passed
    return (new Date()).getTime() - time;
}

function getId(node){ //returns id of the node
    return node.substring(node.lastIndexOf("<") + 1, node.lastIndexOf(">"))   
}

function getLabel(node){//returns label of the node
    return node.replace(/<.*>/, '').replace(/[.*]/, '')
}

function getWeight(node){//returns weight of the node
    return node.substring(node.lastIndexOf("[") + 1, node.lastIndexOf("]"))
}

function updateCurrentCombination(){ //gets the total combination of possible swaps for the given iteration
    currentCombination = (objectSize(leftNodes)-currentIteration)*(objectSize(rightNodes)-currentIteration)
}

function preload(){ //before the canvas script runs
    dataJSON = loadJSON('/static/algorithm_json/KL_data.json'); //gets the JSON
}

function graphData(){
    trace1.x.push(currentIteration)
    trace1.y.push(iteration_data.getIteration(currentIteration).gain)
    trace2.x.push(currentIteration)
    trace2.y.push(iteration_data.getIteration(currentIteration).cutsize)
    Plotly.newPlot('chartContainer', data, layout);
}

function setup() { //sets up the canvas and values for swap
    leftNodes = dataJSON["data"][0]["left_side_unmodified"]
    rightNodes = dataJSON["data"][0]["right_side_unmodified"]

    /*
        ----------------------------------------------------------------------------
        Ignore the two for-loops (they are just finding all the unique weight values)
        ----------------------------------------------------------------------------
    */

    //loops through all the initial left nodes
    for(var node in leftNodes){
        for(var i = 0; i<leftNodes[node].length; i++){
            nodeWeight = getWeight(leftNodes[node][i])
            leftNodes[node][i] = [getId(leftNodes[node][i]), nodeWeight] //splits the id and the weight of the node in a list
            nodes.addWeightColor(nodeWeight);
        }
    }
    //same as the for loop above but for the right nodes
    for(var node in rightNodes){
        for(var i = 0; i<rightNodes[node].length; i++){
            nodeWeight = getWeight(rightNodes[node][i])
            rightNodes[node][i] = [getId(rightNodes[node][i]), nodeWeight]
            nodes.addWeightColor(nodeWeight);
        }
    }

    //For existing node key pairs (ids) that haven't been locked yet
    listLeftNodes = Object.keys(leftNodes);
    listRightNodes = Object.keys(rightNodes);

    for(var i = 0; i < listLeftNodes.length; i++){

        //sets the coordinates of each node
        var x = w*(3/8);
        var y = (h-2*200)*(i/listLeftNodes.length)+200;

        // adds a node to nodes
        nodes.addNode(getId(listLeftNodes[i]), new Node(
            {"initialX": x, "currentX": x}, // x
            {"initialY": y, "currentY": y}, // y
            leftNodes[listLeftNodes[i]], // edges
            getLabel(listLeftNodes[i]), // label
            false // locked
        ))
        
        //pushes existing unlocked id keys to leftNodeKeys
        leftNodeKeys.push(getId(listLeftNodes[i]))
    }

    for(var i = 0; i < listRightNodes.length; i++){
        //sets the coordinates of each node
        var x = w*(5/8);
        var y = (h-2*200)*(i/listRightNodes.length)+200

        // adds a node to nodes
        nodes.addNode(getId(listRightNodes[i]), new Node(
            {"initialX": x, "currentX": x}, // x
            {"initialY": y, "currentY": y}, // y
            rightNodes[listRightNodes[i]], // edges
            getLabel(listRightNodes[i]), // label
            false // locked
        ))
        
        //pushes existing unlocked id keys to leftNodeKeys
        rightNodeKeys.push(getId(listRightNodes[i]))
    }

    //sets up for swap
    maxIteration = Math.max(objectSize(leftNodes), objectSize(rightNodes)) //finds the final iteration
    updateCurrentCombination() //sets the number of swap combinations
    iteration_data = new Data(dataJSON["data"])

    //pushes inital data to the graph
    trace1.x.push(currentIteration)
    trace1.y.push(0)
    trace2.x.push(currentIteration)
    trace2.y.push(dataJSON["data"][currentIteration+1]["cutsize"])
    Plotly.newPlot('chartContainer', data, layout);

    // confirms everything is ready 
    loaded = true;

    //set some default parms
    var canvas = createCanvas(w, h)
    textSize(sizeOfText)
    textAlign(CENTER)
    strokeWeight(5)
}

function draw() {
    background(255, 255, 255);//refreshes when loop back
    if(loaded){
        stroke(0,0,0)
        doProcess()
        drawEdges()
        stroke(0,0,0) //black
        line(windowWidth/2, windowHeight*.2, windowWidth/2, windowHeight*.7)
        nodes.drawAllNodes();
        drawStats()
        startProcess()

    }else{
        textSize(12)
        text("Loading Data", windowWidth/2, windowHeight/2)
        textSize(sizeOfText)
    }
}

function startProcess(){ //if space is pressed the processes will start
    if(keyIsDown(32) && timeSince(inProcess) >= 500){
        if(isProcess){
            //isProcess = false
        }else{
            isProcess = true
            if(!currentIterationTime){
                currentIterationTime = dateInitial()
            }
        }
        inProcess = dateInitial()
    }
}

function drawEdges(){
    for (const [id, node] of Object.entries(nodes.nodes)) {
        x1 = node.x.currentX
        y1 = node.y.currentY

        node.edges.forEach((edge) => {
            otherNode = nodes.findNode(edge.id)
            x2 = otherNode.x.currentX
            y2 = otherNode.y.currentY

            stroke(nodes.weightColors[edge.weight])
            line(x1, y1, x2, y2)
        })
    }

}

function drawStats(){
    textSize(12)
    textAlign(LEFT)
    var i = 0;
    for(var weight in nodes.weightColors){
        stroke(0,0,0)
        strokeWeight(3)
        fill(nodes.weightColors[weight])
        circle(3*windowWidth/4, windowHeight/6+i*32, 16)
        strokeWeight(1)
        fill(0,0,0,0)
        text("Weight: " + String(weight), 3*windowWidth/4+32, windowHeight/6+i*32+4)
        i++;
    }
    text("Current KL Speed: " + String(currentSpeed.toFixed(2)) + "x", 3*windowWidth/4+32, windowHeight/6+(i+1)*32+4)
    textSize(14)
    text("Press space to start", 3*windowWidth/4+32, windowHeight/6+(i+2)*32+4)
    text("Use scroll wheel up and down to control the speed", 3*windowWidth/4+32, windowHeight/6+(i+3)*32+4)
    textSize(sizeOfText)
    textAlign(CENTER)
    strokeWeight(5)
}

function doProcess(){
    if(isProcess && !isfinished){
        swap()
    }
}

function swap(){
    //eachSwapTime = (timeIterSpeed/currentCombination) //do whichSwap = timeSince(currentIterationTime)/eachSwapTime if you want a exponential decay swap time
    whichSwap = timeSince(currentIterationTime)/timeIterSpeed
    if(Math.floor(whichSwap) < currentCombination){
        if(currentSwap != Math.floor(whichSwap)){
            nodes.updateNodeInitial(leftNodeKeys[Math.floor(currentSwap/rightNodeKeys.length)])
            nodes.updateNodeInitial(rightNodeKeys[Math.floor(currentSwap)%rightNodeKeys.length])
        }
        currentSwap = Math.floor(whichSwap)
        swapLeftNodeId = leftNodeKeys[Math.floor(whichSwap/rightNodeKeys.length)]
        swapRightNodeId = rightNodeKeys[Math.floor(whichSwap)%rightNodeKeys.length]

        /*
            Algorithm = (V2-V1)*(timePassed/totalTime)+V1 (this will help with 3rd modeling if implemented)
        */
        nodes.swapNodes(swapLeftNodeId, swapRightNodeId, whichSwap-Math.floor(whichSwap))
    }
    else{//once iteration/comb is done

        //initial updated (TODO: make this a one time event)
        nodes.updateNodeInitial(leftNodeKeys[Math.floor(currentSwap/rightNodeKeys.length)])
        nodes.updateNodeInitial(rightNodeKeys[Math.floor(currentSwap)%rightNodeKeys.length])

        if(!changeIteration){ //swap the locked nodes position
            lockedNodeTimeStart = dateInitial()
            changeIteration = true;
            id_1 = iteration_data.getIteration(currentIteration+1).pair[0]
            id_2 = iteration_data.getIteration(currentIteration+1).pair[1]
            nodes.swapInitial(id_1, id_2)
        }

        if(timeSince(lockedNodeTimeStart) >= maxTimeIterLocked){ //once the nodes are locked
            //locked nodes swapping exact placement
            id_1 = iteration_data.getIteration(currentIteration+1).pair[0]
            id_2 = iteration_data.getIteration(currentIteration+1).pair[1]

            //console.log(id_1, id_2)

            //initial updated
            nodes.updateNodeInitial(id_1)
            nodes.updateNodeInitial(id_2)

            //moves to next iteration
            currentIteration += 1;

            //pairs are locked
            nodes.findNode(id_1).locked = true
            nodes.findNode(id_2).locked = true

            //console.log(leftNodeKeys, rightNodeKeys)

            //removes key pairs from existing unlocked pairs
            leftNodeKeys.splice(leftNodeKeys.indexOf(String(id_1)), 1)
            rightNodeKeys.splice(rightNodeKeys.indexOf(String(id_2)), 1)

            //console.log(leftNodeKeys, rightNodeKeys)

            //resets the current swap in the iteration
            currentSwap = 0
            currentIterationTime = dateInitial()

            //update graph
            graphData()

            if(currentIteration == maxIteration){//once finished
                isfinished = true;
            }else{
                updateCurrentCombination()//update the combination avaliable
            }
            changeIteration = false

        }else{ //swapping of the locked nodes
            id_1 = iteration_data.getIteration(currentIteration+1).pair[0]
            id_2 = iteration_data.getIteration(currentIteration+1).pair[1]
            nodes.swapNodes(id_1, id_2, (timeSince(lockedNodeTimeStart)/maxTimeIterLocked)*.5+.5) // reverse half
        }
    }
}

function mouseWheel(event) { //changes speed of the swap (not implemented yet)
    if(isProcess){
        dSlot = event.delta;
        if(dSlot > 0){ // scroll down
            if(currentSpeed > 1){
                currentSpeed -= deltaSpeed;
                timeIterSpeed = maxTimeIter / currentSpeed
                currentIterationTime = dateInitial() - (whichSwap * timeIterSpeed)
            }
            if(currentSpeed < 1){
                currentSpeed = 1
            }
        }else{ //scroll up
            if(currentSpeed < maxSpeed){
                currentSpeed += deltaSpeed;
                timeIterSpeed = maxTimeIter / currentSpeed
                currentIterationTime = dateInitial() - (whichSwap * timeIterSpeed)
            }
            if(currentSpeed > maxSpeed){
                currentSpeed = maxSpeed
            }
        }
    }
}

//window resize done
function windowResized() {
    resizeCanvas(windowWidth, windowHeight)
    nodes.resize(windowWidth/w, windowHeight/h)
    w = window.innerWidth
    h = window.innerHeight
}
