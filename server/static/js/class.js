
// classes for nodes
class Nodes {
    constructor() {
        this.nodes = [];
    }

    addNode(node){
        this.nodes.push(node)
    }

    getNode(index){
        return this.nodes[index]
    }

    findNode(id){
        var idNode
        this.nodes.forEach((node) => {
            if(node.id == id){
                idNode = node
            }
        })
        return idNode
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

        v1 = createVector(node_1.x.intialX, node_1.y.intialY) // left
        v2 = createVector(node_2.x.intialX, node_2.y.intialY) // right
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

        var coords_1 = node_1.getIntial()
        var coords_2 = node_2.getIntial()

        // x
        node_1.x.intialX = coords_2[0]
        node_2.x.intialX = coords_1[0]

        // y
        node_1.y.intialY = coords_2[1]
        node_2.y.intialY = coords_1[1]
    }

    updateNodeIntial(id){
        var node = this.findNode(id)
        node.updateX(node.x.intialX)
        node.updateY(node.y.intialY)
    }
}

class Node {
    constructor(id, x, y, edges, label, locked) {
        this.id = id;
        this.x = x;
        this.y = y;
        this.edges = [];
        for (var i = 0; i < edges.length; i++){
            this.edges.push(new Edge(edges[i][0], edges[i][1]))
        }
        this.label = label;
        this.locked = locked;
    }

    updateX(x){
        this.x.currentX = x
    }

    updateY(y){
        this.y.currentY = y
    }

    getIntial(){
        return [this.x.intialX, this.y.intialY]
    }
}

class Edge {
    constructor(id, weight) {
        this.id = id;
        this.weight = weight;
    }
}

class Data {
    constructor(data){
        this.iterations = []
        for(var i = 1; i < data.length; i++){
            if(typeof data[i]["gain"] == 'undefined'){
                this.iterations.push(new Iteration(data[i]["cutsize"], null, null, null))
            }else{
                this.iterations.push(new Iteration(data[i]["cutsize"], data[i]["gain"], data[i]["pair"], data[i]["swap_time"]))
            }
        }
    }

    getIteration(index){
        return this.iterations[index]
    }
}

class Iteration {
    constructor(cutsize, gain, pair, swap_time){
        this.cutsize = cutsize
        this.gain = gain
        this.pair = pair
        this.swap_time = swap_time
    }
}