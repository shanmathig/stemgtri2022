//global variables for use throughout canvas draw
let w = window.innerWidth
let h = window.innerHeight
let loaded = false
let isProcess = false
var maxSpeed = 10;
var currentSpeed = 1;
var inProcess = dateIntial()
var sizeOfCircle = 64
var sizeOfText = 36
var dataJSON
let leftNodes
let rightNodes
var nodes = {}
var currentIterationTime
var currentIteration = 0
var maxIteration
var currentCombination
var isfinished = false
var maxTimeIter = 500
var currentNodes = [0,0];
var leftNodeKeys = [];
var rightNodeKeys = [];
var currentSwap = 0;
var lockedSwap = false
var changeIteration = false;
var lockedNodeTimeStart;
var weightColors = {}

//functions used throughout the process
function objectSize(obj) {//returns a javascript object (dict) size
    var size = 0,
    key
    for (key in obj) {
        if (obj.hasOwnProperty(key)) size++;
    }
    return size;
};

function dateIntial(){ //returns an int of the time
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

function setup() { //sets up the canvas and values for swap
    leftNodes = dataJSON["data"][0]["left_side_unmodified"]
    rightNodes = dataJSON["data"][0]["right_side_unmodified"]
    //loops through all the intial left nodes
    for(var node in leftNodes){
        for(var i = 0; i<leftNodes[node].length; i++){
            nodeWeight = getWeight(leftNodes[node][i])
            leftNodes[node][i] = [getId(leftNodes[node][i]), nodeWeight] //splits the id and the weight of the node in a list
            if(!weightColors.hasOwnProperty(nodeWeight)){ //if the weight isn't recorded
                weightColors[nodeWeight] = color(Math.floor(random(255)), Math.floor(random(255)), Math.floor(random(255))) //weight is assigned random color
            }
        }
    }
    //same as the for loop above but for the right nodes
    for(var node in rightNodes){
        for(var i = 0; i<rightNodes[node].length; i++){
            nodeWeight = getWeight(rightNodes[node][i])
            rightNodes[node][i] = [getId(rightNodes[node][i]), nodeWeight]
            if(!weightColors.hasOwnProperty(nodeWeight)){
                weightColors[nodeWeight] = color(Math.floor(random(255)), Math.floor(random(255)), Math.floor(random(255))) 
            }
        }
    }
    listLeftNodes = Object.keys(leftNodes);
    listRightNodes = Object.keys(rightNodes);
    for(var i = 0; i < listLeftNodes.length; i++){
        //sets the coordinates of each node
        var x = w*(3/8);
        var y = (h-2*200)*(i/listLeftNodes.length)+200;
        // {"id": [{"intialX": x, "currentX": x}, {"intialY": y, "currentY": y}, weight-info, label, locked]}
        nodes[getId(listLeftNodes[i])] = [{"intialX": x, "currentX": x}, {"intialY": y, "currentY": y}, leftNodes[listLeftNodes[i]], getLabel(listLeftNodes[i]), false];
        leftNodeKeys.push(getId(listLeftNodes[i]))
    }
    //same as the above for loop
    for(var i = 0; i < listRightNodes.length; i++){
        var x = w*(5/8);
        var y = (h-2*200)*(i/listRightNodes.length)+200
        nodes[getId(listRightNodes[i])] = [{"intialX": x, "currentX": x}, {"intialY": y, "currentY": y}, rightNodes[listRightNodes[i]], getLabel(listRightNodes[i]), false];
        rightNodeKeys.push(getId(listRightNodes[i]))
    }
    maxIteration = Math.max(objectSize(leftNodes), objectSize(rightNodes)) //finds the final iteration
    updateCurrentCombination() //sets the number of swap combinations
    //pushes data to the graph
    trace1.x.push(currentIteration)
    trace1.y.push(0)
    trace2.x.push(currentIteration)
    trace2.y.push(dataJSON["data"][currentIteration+1]["cutsize"])
    Plotly.newPlot('chartContainer', data, layout);
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
        line(windowWidth/2, windowHeight*.2, windowWidth/2, windowHeight*.7)
        doProcess()
        drawEdges()
        drawNodes()
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
                currentIterationTime = dateIntial()
            }
        }
        inProcess = dateIntial()
    }
}

function drawEdges(){
    for(var node in nodes){
        [x1, y1, edges] = nodes[node];
        for(var i = 0; i < edges.length; i++){
            [x2, y2] = nodes[edges[i][0]];
            stroke(weightColors[edges[i][1]])
            line(x1["currentX"], y1["currentY"], x2["currentX"], y2["currentY"])
        }
    }
}

function drawNodes(){
    for(var node in nodes){
        [x, y, _, label, locked] = nodes[node];
        fill(255,255,255)
        if(locked){
            stroke(0,255,0)
            circle(x["currentX"], y["currentY"], sizeOfCircle)
            stroke(0,0,0)
        }else{
            stroke(0,0,0)
            circle(x["currentX"], y["currentY"], sizeOfCircle)
        }
        noStroke()
        fill(0,0,0)
        text(label, x["currentX"], y["currentY"]+sizeOfText/4)
    }
}

function drawStats(){
    textSize(12)
    textAlign(LEFT)
    var i = 0;
    for(var weight in weightColors){
        stroke(0,0,0)
        strokeWeight(3)
        fill(weightColors[weight])
        circle(3*windowWidth/4, windowHeight/6+i*32, 16)
        strokeWeight(1)
        fill(0,0,0,0)
        text("Weight: " + String(weight), 3*windowWidth/4+32, windowHeight/6+i*32+4)
        i++;
    }
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
    //eachSwapTime = (maxTimeIter/currentCombination) do whichSwap = timeSince(currentIterationTime)/eachSwapTime if you want a exponential decay swap time
    whichSwap = timeSince(currentIterationTime)/maxTimeIter
    if(Math.floor(whichSwap) < currentCombination){
        if(currentSwap != Math.floor(whichSwap)){
            swapLeftNode = nodes[leftNodeKeys[Math.floor(currentSwap/rightNodeKeys.length)]]
            swapRightNode = nodes[rightNodeKeys[Math.floor(currentSwap)%rightNodeKeys.length]]
            swapLeftNode[0]["currentX"] = swapLeftNode[0]["intialX"]
            swapLeftNode[1]["currentY"] = swapLeftNode[1]["intialY"]
            swapRightNode[0]["currentX"] = swapRightNode[0]["intialX"]
            swapRightNode[1]["currentY"] = swapRightNode[1]["intialY"]
        }
        currentSwap = Math.floor(whichSwap)
        swapLeftNode = nodes[leftNodeKeys[Math.floor(whichSwap/rightNodeKeys.length)]]
        swapRightNode = nodes[rightNodeKeys[Math.floor(whichSwap)%rightNodeKeys.length]]
        //use the console logs below to debug any nodes
        //console.log(nodes[leftNodeKeys[Math.floor(whichSwap/rightNodeKeys.length)]][3], nodes[rightNodeKeys[Math.floor(whichSwap)%rightNodeKeys.length]][3], Math.floor(whichSwap/rightNodeKeys.length), Math.floor(whichSwap)%rightNodeKeys.length)
        //console.log(nodes[swapLeftNode][3], nodes[swapRightNode][3])
        /*
            Algorithm = (V2-V1)*(timePassed/totalTime)+V1 (this will help with 3rd modeling if implemented)
        */
        if(whichSwap-Math.floor(whichSwap) <= .5){ //first half of swap
            //left node movement by time
            v1 = createVector(swapLeftNode[0]["intialX"], swapLeftNode[1]["intialY"])
            v2 = createVector(swapRightNode[0]["intialX"], swapRightNode[1]["intialY"])
            v3 = (v2.sub(v1)).mult(2*(whichSwap-Math.floor(whichSwap))).add(v1)
            swapLeftNode[0]["currentX"] = v3.x
            swapLeftNode[1]["currentY"] = v3.y

            //right node movement by time
            v1 = createVector(swapLeftNode[0]["intialX"], swapLeftNode[1]["intialY"])
            v2 = createVector(swapRightNode[0]["intialX"], swapRightNode[1]["intialY"])
            v3 = (v1.sub(v2)).mult(2*(whichSwap-Math.floor(whichSwap))).add(v2)
            swapRightNode[0]["currentX"] = v3.x
            swapRightNode[1]["currentY"] = v3.y
        }else{ //then back
            //left node movement by time
            v1 = createVector(swapLeftNode[0]["intialX"], swapLeftNode[1]["intialY"])
            v2 = createVector(swapRightNode[0]["intialX"], swapRightNode[1]["intialY"])
            v3 = (v1.sub(v2)).mult(2*(whichSwap-Math.floor(whichSwap)-.5)).add(v2)
            swapLeftNode[0]["currentX"] = v3.x
            swapLeftNode[1]["currentY"] = v3.y

            //right node movement by time
            v1 = createVector(swapLeftNode[0]["intialX"], swapLeftNode[1]["intialY"])
            v2 = createVector(swapRightNode[0]["intialX"], swapRightNode[1]["intialY"])
            v3 = (v2.sub(v1)).mult(2*(whichSwap-Math.floor(whichSwap)-.5)).add(v1)
            swapRightNode[0]["currentX"] = v3.x
            swapRightNode[1]["currentY"] = v3.y
        }
    }
    else{//once iteration/comb is done
        swapLeftNode = nodes[leftNodeKeys[Math.floor(currentSwap/rightNodeKeys.length)]]
        swapRightNode = nodes[rightNodeKeys[Math.floor(currentSwap)%rightNodeKeys.length]]
        swapLeftNode[0]["currentX"] = swapLeftNode[0]["intialX"]
        swapLeftNode[1]["currentY"] = swapLeftNode[1]["intialY"]
        swapRightNode[0]["currentX"] = swapRightNode[0]["intialX"]
        swapRightNode[1]["currentY"] = swapRightNode[1]["intialY"]
        if(!changeIteration){ //swap the locked nodes position
            lockedNodeTimeStart = dateIntial()
            changeIteration = true;
            someX1 = nodes[dataJSON["data"][currentIteration+2]["pair"][0]][0]["intialX"]
            someY1 = nodes[dataJSON["data"][currentIteration+2]["pair"][0]][1]["intialY"]
            someX2 = nodes[dataJSON["data"][currentIteration+2]["pair"][1]][0]["intialX"]
            someY2 = nodes[dataJSON["data"][currentIteration+2]["pair"][1]][1]["intialY"]
            nodes[dataJSON["data"][currentIteration+2]["pair"][0]][0]["intialX"] = someX2
            nodes[dataJSON["data"][currentIteration+2]["pair"][0]][1]["intialY"] = someY2
            nodes[dataJSON["data"][currentIteration+2]["pair"][1]][0]["intialX"] = someX1
            nodes[dataJSON["data"][currentIteration+2]["pair"][1]][1]["intialY"] = someY1
        }
        if(timeSince(lockedNodeTimeStart) >= maxTimeIter){
            //locked nodes swaping exact placement
            nodes[dataJSON["data"][currentIteration+2]["pair"][0]][0]["currentX"] = nodes[dataJSON["data"][currentIteration+2]["pair"][0]][0]["intialX"]
            nodes[dataJSON["data"][currentIteration+2]["pair"][0]][1]["currentY"] = nodes[dataJSON["data"][currentIteration+2]["pair"][0]][1]["intialY"]
            nodes[dataJSON["data"][currentIteration+2]["pair"][1]][0]["currentX"] = nodes[dataJSON["data"][currentIteration+2]["pair"][1]][0]["intialX"]
            nodes[dataJSON["data"][currentIteration+2]["pair"][1]][1]["currentY"] = nodes[dataJSON["data"][currentIteration+2]["pair"][1]][1]["intialY"]
            currentIteration += 1;
            //console.log(currentIteration)
            //pairs are locked
            nodes[dataJSON["data"][currentIteration+1]["pair"][0]][4] = true
            nodes[dataJSON["data"][currentIteration+1]["pair"][1]][4] = true
            leftNodeKeys.splice(leftNodeKeys.indexOf(String(dataJSON["data"][currentIteration+1]["pair"][0])), 1)
            rightNodeKeys.splice(rightNodeKeys.indexOf(String(dataJSON["data"][currentIteration+1]["pair"][1])), 1)
            currentSwap = 0
            currentIterationTime = dateIntial()
            whichSwap = timeSince(currentIterationTime)
            //update graph
            trace1.x.push(currentIteration)
            trace1.y.push(dataJSON["data"][currentIteration+1]["gain"])
            trace2.x.push(currentIteration)
            trace2.y.push(dataJSON["data"][currentIteration+1]["cutsize"])
            Plotly.newPlot('chartContainer', data, layout);

            if(currentIteration == maxIteration){//once finished
                isfinished = true;
            }else{
                updateCurrentCombination()//update the combination avaliable
            }
            changeIteration = false
        }else{ //swaping of the locked nodes
            v1 = createVector(nodes[dataJSON["data"][currentIteration+2]["pair"][0]][0]["intialX"], nodes[dataJSON["data"][currentIteration+2]["pair"][0]][1]["intialY"])
            v2 = createVector(nodes[dataJSON["data"][currentIteration+2]["pair"][1]][0]["intialX"], nodes[dataJSON["data"][currentIteration+2]["pair"][1]][1]["intialY"])
            v3 = (v1.sub(v2)).mult(timeSince(lockedNodeTimeStart)/maxTimeIter).add(v2)
            nodes[dataJSON["data"][currentIteration+2]["pair"][0]][0]["currentX"] = v3.x
            nodes[dataJSON["data"][currentIteration+2]["pair"][0]][1]["currentY"] = v3.y

            v1 = createVector(nodes[dataJSON["data"][currentIteration+2]["pair"][0]][0]["intialX"], nodes[dataJSON["data"][currentIteration+2]["pair"][0]][1]["intialY"])
            v2 = createVector(nodes[dataJSON["data"][currentIteration+2]["pair"][1]][0]["intialX"], nodes[dataJSON["data"][currentIteration+2]["pair"][1]][1]["intialY"])
            v3 = (v2.sub(v1)).mult(timeSince(lockedNodeTimeStart)/maxTimeIter).add(v1)
            nodes[dataJSON["data"][currentIteration+2]["pair"][1]][0]["currentX"] = v3.x
            nodes[dataJSON["data"][currentIteration+2]["pair"][1]][1]["currentY"] = v3.y
        }
    }
}

function mouseWheel(event) { //changes speed of the swap (not implemented yet)
    dSlot = event.delta;
    if(dSlot > 0){ // scroll down
        if(currentSpeed != 1){
            currentSpeed -= 1;
        }else{
            currentSpeed = maxSpeed;
        }
    }else{ //scroll up
        if(currentSpeed != maxSpeed){
            currentSpeed += 1;
        }else{
            currentSpeed = 1;
        }
    }
}

/* buggy because position matters
//window resize done
function windowResized() {
    resizeCanvas(windowWidth, windowHeight)
    w = window.innerWidth
    h = window.innerHeight
    listLeftNodes = Object.keys(leftNodes);
    listRightNodes = Object.keys(rightNodes);
    for(var i = 0; i < listLeftNodes.length; i++){
        var x = w*(3/8);
        var y = (h-2*250)*(i/listLeftNodes.length)+250;
        nodes[getId(listLeftNodes[i])] = [{"intialX": x, "currentX": x}, {"intialY": y, "currentY": y}, leftNodes[listLeftNodes[i]], getLabel(listLeftNodes[i]), false];
    }
    for(var i = 0; i < listRightNodes.length; i++){
        var x = w*(5/8);
        var y = (h-2*250)*(i/listRightNodes.length)+250
        nodes[getId(listRightNodes[i])] = [{"intialX": x, "currentX": x}, {"intialY": y, "currentY": y}, rightNodes[listRightNodes[i]], getLabel(listRightNodes[i]), false];
    }
}*/