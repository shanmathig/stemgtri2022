//functions used throughout the process
function objectSize(obj) {//returns a javascript object (dict) size
    var size = 0,
    key
    for (key in obj) {
        if (obj.hasOwnProperty(key)) size++;
    }
    return size;
};

function updateCurrentCombination(){ //gets the total combination of possible swaps for the given iteration
    currentCombination = (objectSize(leftNodes)-currentIteration)*(objectSize(rightNodes)-currentIteration)
}

function timeSince(time){ //returns an int of how much time has passed
    return (new Date()).getTime() - time;
}

function dateInitial(){ //returns an int of the time
    return (new Date()).getTime();
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
