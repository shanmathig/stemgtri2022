//global variables for use throughout canvas draw
let jsonData;
let w = window.innerWidth;
let h = window.innerHeight;
var whichMincutSwap = 0;
var moveNodeDelayTimer = 0;

var quadrantHolder = new QuadrantManager();

var currentIter = 0;

var inMincutProcess;

const sizeOfCircle = 64;
const sizeOfText = 36;

var cutIter = 0;
var ran = false;

var isMincutDone = true;

var currentMincutIterationTime = dateInitial();
var maxMincutTimeIter = 500;
var continueUpdatingAfterFinish = false;
var checkCompletionOfMincut = true;
var mincutIterationData;
var whatsHappening = 'Nodes are randomly arranged';

// KL variables
let loaded = false
let isProcess = false
var maxSpeed = 100
var currentSpeed = 1
var deltaSpeed = .1
var inProcess = dateInitial()
var dataJSON
let leftNodes
let rightNodes
var currentIterationTime
var currentIteration = 0
var maxIteration
var currentCombination
var isfinished = false
var maxTimeIter = 5000
var timeIterSpeed = maxTimeIter / currentSpeed
var maxTimeIterLocked = 1000
var leftNodeKeys = []
var rightNodeKeys = []
var originalLeftNodeKeys = []
var originalRightNodeKeys = []
var currentSwap = 0
var changeIteration = false
var lockedNodeTimeStart
var iteration_data
var nodes = new Nodes();
var whichSwap = undefined;

function preload() {
    jsonData = loadJSON('/static/algorithm_json/mincut_data.json');
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
    textSize(50)
    fill(0,0,0)
    textSize(50)
    textAlign(CENTER)
    text(whatsHappening, 4*windowWidth/8, 7.5*windowHeight/8)
    textSize(sizeOfText)
    strokeWeight(5)
}

function setup() {
    var canvas = createCanvas(w, h);
    textSize(sizeOfText);
    textAlign(CENTER)
    strokeWeight(5)
    frameRate(60);
    print(jsonData['data']);

    // setup the mincut data
    mincutIterationData = new MincutCutData(jsonData['data']);

    print(mincutIterationData);

    // creates initial quadrant that will later be split
    var initialQuadrant = new Quadrant(
        (3*w/8 + 10) * 0 + w/8, // x
        50 * 0 + h/8, // y
        6*w/8, // width
        6*h/8, // height
        6*w/8, // targetWidth
        6*h/8, // targetHeight
        0, // gridX
        0 //gridY
    )
    quadrantHolder.addQuadrant(initialQuadrant);

    // adds all nodes
    for (nodeKey in jsonData['data'][0]) {
        var edges = jsonData['data'][0][nodeKey];
        var nodeId = getId(nodeKey);
        var nodeLabel = getLabel(nodeKey);

        var KLedges = [];

        // sets up tracking for weight colors
        for(var i = 0; i < edges.length; i++){
            edgeWeight = getWeight(edges[i]);
            edgeId = getId(edges[i]);
            KLedges.push([edgeId, edgeWeight])
            nodes.addWeightColor(edgeWeight);
        }

        nodes.addNode(nodeId.toString(), new Node(
            {'initialX': null, 'currentX': null}, // x
            {'initialY': null, 'currentY': null}, // y
            KLedges, // edges
            nodeLabel, // label
            false, // locked
            Math.floor(Math.random() * (7*w/8 - w/8) + w/8), // mincutX
            Math.floor(Math.random() * (7*h/8 - h/8) + h/8), // mincutY
            nodeId, // id
        ))   
    }

    // initially starts with mincut
    nodes.setMincutProcess(true);
    //inMincutProcess = true;
    // confirms everything is ready 
    loaded = true;
}

function runProcess() {
    if (!continueUpdatingAfterFinish) {
        // currentIter is basically the depth of the recursive cuts        
        quadrantHolder.updateAndAddQuadrants(currentIter, mincutIterationData);
    }
}

function loadKLData() {
    dataJSON = mincutIterationData.getKLSequence(currentIter, cutIter);

    leftNodes = dataJSON["data"][0]["left_side_unmodified"]
    rightNodes = dataJSON["data"][0]["right_side_unmodified"]


    //loops through all the initial left nodes
    for(var node in leftNodes){
        for(var i = 0; i<leftNodes[node].length; i++){
            nodeWeight = getWeight(leftNodes[node][i])
            leftNodes[node][i] = [getId(leftNodes[node][i]), nodeWeight] //splits the id and the weight of the node in a list
        }
    }
    //same as the for loop above but for the right nodes
    for(var node in rightNodes){
        for(var i = 0; i<rightNodes[node].length; i++){
            nodeWeight = getWeight(rightNodes[node][i])
            rightNodes[node][i] = [getId(rightNodes[node][i]), nodeWeight]
        }
    }

    //For existing node key pairs (ids) that haven't been locked yet
    listLeftNodes = Object.keys(leftNodes);
    listRightNodes = Object.keys(rightNodes);
    leftNodeKeys = [];
    rightNodeKeys = [];

    for(var i = 0; i < listLeftNodes.length; i++){

        var currentNodeId = getId(listLeftNodes[i])    
        
        //pushes existing unlocked id keys to leftNodeKeys
        leftNodeKeys.push(currentNodeId)
    }



    for(var i = 0; i < listRightNodes.length; i++){

        var currentNodeId = getId(listRightNodes[i]);

        //pushes existing unlocked id keys to leftNodeKeys
        rightNodeKeys.push(currentNodeId)
    }


    originalLeftNodeKeys = Array.from(leftNodeKeys)
    originalRightNodeKeys = Array.from(rightNodeKeys)


    // initializes x and y positions for KL
    nodes.setKLXAndY(leftNodeKeys, rightNodeKeys);


    //sets up for swap
    maxIteration = Math.max(objectSize(leftNodes), objectSize(rightNodes)) //finds the final iteration
    updateCurrentCombination() //sets the number of swap combinations
    iteration_data = new Data(dataJSON["data"])


    //var canvas = createCanvas(w, h);
    textSize(sizeOfText)
    textAlign(CENTER)
    strokeWeight(5)
}

function draw() {
    background(255, 255, 255);

    if (!currentMincutIterationTime) {
        currentMincutIterationTime = dateInitial()
    }

    // waits for spacebar to be pressed
    if (loaded) {
        startProcess();
    }
    
    runMincutProcess();

    isMincutDone = true;

    // draws quadrants, edges, and nodes
    quadrantHolder.drawQuadrants();
    nodes.drawAllEdges(checkCompletionOfMincut);
    nodes.drawAllNodes(checkCompletionOfMincut);
    isMincutDone = nodes.getMincutStatus();

    drawStats();
    if(isProcess && !isfinished){
        swap();
    }

    if (isMincutDone && !continueUpdatingAfterFinish && checkCompletionOfMincut) {
        prepareForKL();
    }
}

function runMincutProcess() {
    whichMincutSwap = timeSince(currentMincutIterationTime) / maxMincutTimeIter;
    
    // adds small 2.5 second delay before running KL at a new recursion depth
    if (Math.floor(whichMincutSwap) > 2.5 && currentIter <= Object.keys(nodes.nodes).length ** (1/2)) {

        // runs process of splitting quadrants for current recursion depth
        if (!ran) {
            runProcess();
            ran = true;
        }
        
        // add a delay so that all quadrants for a given recursion depth are not made at once
        // runs only if mincut is happening and has not finished
        if (inMincutProcess && !continueUpdatingAfterFinish && millis() >= (7500/mincutIterationData.getNumQuadrantsInIterDepth(currentIter))+moveNodeDelayTimer) {
            whatsHappening = 'Running mincut algorithm';

            // coords and nodes for group 1 of the mincut split
            var { x_coord, y_coord } = mincutIterationData.getGroupCoords(currentIter, cutIter, 'group_1_coords');
            var groupNodes = mincutIterationData.getGroupNodes(currentIter, cutIter, 'group_1_nodes');

            // begins shrinking rectangle/quadrant containing the nodes in group 1
            quadrantHolder.startShrinking(x_coord, y_coord, groupNodes.map(getId), nodes);
            

            // coords and nodes for group 2 of the mincut split
            var { x_coord, y_coord } = mincutIterationData.getGroupCoords(currentIter, cutIter, 'group_2_coords');
            var groupNodes = mincutIterationData.getGroupNodes(currentIter, cutIter, 'group_2_nodes');

            // begins shrinking the rectangle/quadrant containing the nodes in group 2
            quadrantHolder.startShrinking(x_coord, y_coord, groupNodes.map(getId), nodes);

            
            /*
                LOADS IN KL DATA
            */
            loadKLData();
            /*
                END OF LOADING IN OF KL DATA
            */


            // tracks when mincut nodes are at intended positions
            checkCompletionOfMincut = true;

            
            cutIter += 1;
            moveNodeDelayTimer = millis();

            // waits for a given recursion depth to be fully finished & resets variables once it is
            if (mincutIterationData.iterationData[currentIter] == undefined || cutIter >= mincutIterationData.iterationData[currentIter].length) {
                cutIter = 0;
                whichMincutSwap = 0;
                currentMincutIterationTime = dateInitial();
                currentIter += 1;
                ran = false;
            }
        }
    }
}

function prepareForKL() {
    // sets variables to prepare for the start of KL
    checkCompletionOfMincut = false;
    nodes.setMincutProcess(false);
    inMincutProcess = false;
    whatsHappening = 'Running Kernighan-Lin algorithm';
    isfinished = false;
    isProcess = true;
    isMincutDone = true;
    if(!currentIterationTime){
        currentIterationTime = dateInitial()
    }
    inProcess = dateInitial()
}

function prepareForMincut() {
    // sets variables to prepare for the start of next iteration of mincut
    nodes.updateMincutPositions(originalLeftNodeKeys, originalRightNodeKeys);
    currentIteration = 0;
    isProcess = false;
    isfinished = true;
    inMincutProcess = true;
    whatsHappening = 'Reverting KL to step with optimal cutsize';
    nodes.setMincutProcess(true);
    whichMincutSwap = 0;
    currentMincutIterationTime = dateInitial();      
    nodes.unlockAllNodes();

    checkMincutCompletion();
}

function checkMincutCompletion() {
    // runs once mincut is fully done
    if ((currentIter >= Object.keys(nodes.nodes).length ** (1/2))) {
        inMincutProcess = false;
        //isProcess = false;
        continueUpdatingAfterFinish = true;
        nodes.unlockAllNodes();
        whatsHappening = 'Done with placement & partitioning!';
    }
}

function swap(){
    // runs KL
    //eachSwapTime = (maxTimeIter/currentCombination) do whichSwap = timeSince(currentIterationTime)/eachSwapTime if you want a exponential decay swap time
    whichSwap = timeSince(currentIterationTime)/timeIterSpeed
    if(Math.floor(whichSwap) < currentCombination){
        if(currentSwap != Math.floor(whichSwap)){
            nodes.updateNodeInitial(leftNodeKeys[Math.floor(currentSwap/rightNodeKeys.length)])
            nodes.updateNodeInitial(rightNodeKeys[Math.floor(currentSwap)%rightNodeKeys.length])
        }
        currentSwap = Math.floor(whichSwap)
        swapLeftNodeId = leftNodeKeys[Math.floor(whichSwap/rightNodeKeys.length)]
        swapRightNodeId = rightNodeKeys[Math.floor(whichSwap)%rightNodeKeys.length]

        // Algorithm = (V2-V1)*(timePassed/totalTime)+V1 (this will help with 3rd modeling if implemented)
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
            //locked nodes swaping exact placement
            id_1 = iteration_data.getIteration(currentIteration+1).pair[0]
            id_2 = iteration_data.getIteration(currentIteration+1).pair[1]

            //initial updated
            nodes.updateNodeInitial(id_1)
            nodes.updateNodeInitial(id_2)

            //moves to next iteration
            currentIteration += 1;

            //pairs are locked
            nodes.findNode(id_1).locked = true
            nodes.findNode(id_2).locked = true

            //removes key pairs from existing unlocked pairs
            leftNodeKeys.splice(leftNodeKeys.indexOf(String(id_1)), 1)
            rightNodeKeys.splice(rightNodeKeys.indexOf(String(id_2)), 1)

            //resets the current swap in the iteration
            currentSwap = 0
            currentIterationTime = dateInitial()

            if(currentIteration == maxIteration){//once finished
                prepareForMincut();
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

function startProcess(){ //if space is pressed the processes will start
    if(keyIsDown(32) && timeSince(inProcess) >= 500){
        if(isProcess){
            //isProcess = false
        }else{
            inMincutProcess = true;
            
        }
        inProcess = dateInitial()
    }
}

function mouseWheel(event) { //changes speed of the swap (not implemented yet)
    if(!continueUpdatingAfterFinish && whichSwap !== undefined){
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
/*function windowResized() {
    resizeCanvas(windowWidth, windowHeight)
    nodes.resize(windowWidth/w, windowHeight/h)
    w = window.innerWidth
    h = window.innerHeight
}*/