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
var someDict = {}
var currentSwap1
var currentSwap2
var currentIterationTime
var currentIteration = 0
var maxIteration
var currentCombination
var isfinished = false
var maxTimeIter = 2000
var currentNodes = [0,0];
var leftNodeKeys = [];
var rightNodeKeys = [];

function objectSize(obj) {
    var size = 0,
    key
    for (key in obj) {
        if (obj.hasOwnProperty(key)) size++;
    }
    return size;
};

function dateIntial(){
    return (new Date()).getTime();
}

function timeSince(time){
    return (new Date()).getTime() - time;
}

function getId(node){
    return node.substring(node.lastIndexOf("<") + 1, node.lastIndexOf(">"))   
}

function getLabel(node){
    return node.replace(/<.*>/, '')
}

function updateCurrentCombination(){
    currentCombination = (objectSize(leftNodes)-currentIteration)*(objectSize(rightNodes)-currentIteration)
}

function preload(){
    $.getJSON('/static/algorithm_json/KL_data.json', function(data) {
        dataJSON = data;
        leftNodes = dataJSON["data"][0]["left_side_unmodified"]
        rightNodes = dataJSON["data"][0]["right_side_unmodified"]
        for(var node in leftNodes){
            for(var i = 0; i<leftNodes[node].length; i++){
                leftNodes[node][i] = getId(leftNodes[node][i])
            }
        }
        for(var node in rightNodes){
            for(var i = 0; i<rightNodes[node].length; i++){
                rightNodes[node][i] = getId(rightNodes[node][i])
            }
        }
        listLeftNodes = Object.keys(leftNodes);
        listRightNodes = Object.keys(rightNodes);
        for(var i = 0; i < listLeftNodes.length; i++){
            var x = w*(3/8);
            var y = (h-2*250)*(i/listLeftNodes.length)+250;
            someDict[getId(listLeftNodes[i])] = [x, y, leftNodes[listLeftNodes[i]], getLabel(listLeftNodes[i])];
            leftNodeKeys.push(getId(listLeftNodes[i]))
        }
        for(var i = 0; i < listRightNodes.length; i++){
            var x = w*(5/8);
            var y = (h-2*250)*(i/listRightNodes.length)+250
            someDict[getId(listRightNodes[i])] = [x, y, rightNodes[listRightNodes[i]], getLabel(listLeftNodes[i])];
            rightNodeKeys.push(getId(listRightNodes[i]))
        }
        currentSwap1 = getId(listLeftNodes[0]);
        currentSwap2 = getId(listRightNodes[0]);
        maxIteration = Math.max(objectSize(leftNodes), objectSize(rightNodes))
        updateCurrentCombination()
        loaded = true;
    });
}

function setup() {
    var canvas = createCanvas(w, h)
    textSize(sizeOfText)
    textAlign(CENTER)
    strokeWeight(5)
}

function draw() {
    background(255, 255, 255);
    if(loaded){
        //doProcess()
        drawEdges()
        drawNodes()
        drawStats()
        if(mouseIsPressed && timeSince(inProcess) >= 500){
            if(isProcess){
                isProcess = false
            }else{
                isProcess = true
                if(!currentIterationTime){
                    currentIterationTime = dateIntial()
                }
            }
            inProcess = dateIntial()
        }

    }else{
        textSize(12)
        text("Loading JSON", windowWidth/2, windowHeight/2)
        textSize(sizeOfText)
    }
}

function drawEdges(){
    for(var node in someDict){
        [x1, y1, edges] = someDict[node];
        for(var i = 0; i < edges.length; i++){
            [x2, y2] = someDict[edges[i]];
            line(x1, y1, x2, y2)
        }
    }
}

function drawNodes(){
    for(var node in someDict){
        [x, y, _, label] = someDict[node];
        circle(x, y, sizeOfCircle)
        text(label, x, y+sizeOfText/4)
    }
}

function drawStats(){

}

function doProcess(){
    if(isProcess && !isfinished){
        if(timeSince(currentIterationTime) >= maxTimeIter && currentIteration < maxIteration){
            currentIteration += 1;
            currentIterationTime = dateIntial()
            if(currentIteration == maxIteration){
                isfinished = true;
            }else{
                updateCurrentCombination()
            }
        }
        swap()
    }
}

function swap(){
    eachSwapTime = (maxTimeIter/currentCombination)
    whichSwap = timeSince(currentIterationTime)/eachSwapTime
    if(Math.floor(whichSwap) < currentCombination){
        leftNodeKeys[Math.floor(whichSwap/rightNodeKeys.length)]
        rightNodeKeys[whichSwap%rightNodeKeys.length]
    }else{

    }
}

function mouseWheel(event) { 
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
        someDict[getId(listLeftNodes[i])] = [x, y, leftNodes[listLeftNodes[i]], getLabel(listLeftNodes[i])];
    }
    for(var i = 0; i < listRightNodes.length; i++){
        var x = w*(5/8);
        var y = (h-2*250)*(i/listRightNodes.length)+250
        someDict[getId(listRightNodes[i])] = [x, y, rightNodes[listRightNodes[i]], getLabel(listLeftNodes[i])];
    }
}