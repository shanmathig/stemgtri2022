class Chip:
    dimensions : tuple
    nodes : list
    wires : list
    def __init__(self,dimensions):
        self.dimensions = dimensions
        self.nodes = []
        self.wires = []
    def AddNode(self,node):
        self.nodes.append(node)

    def AddWire(self,wire):
        self.wires.append(wire)

class Node:
    logictype : str
    inputs : list
    outputs : list
    name : str
    location : tuple

    #mayhaps this could be improved, but
    #will instantiate the node and put it on the chip list

    def __init__(self,logictype,name,location,chip):
        self.logictype = logictype
        self.name = name
        self.location = location
        #to do: make it so if it doesnt fit on the chip then it will just set it to 0,0 or something
        chip.AddNode(self)

    def AddOutput(self,wire):
        self.outputs.append(wire) 

    def AddInput(self,wire):
        self.inputs.append(wire)

class Wire:
    start : tuple
    end : list #end is a list of tuples since there could be multiple endpoints
    length : int

    def __init__(self,length,start,end,chip):
        self.length = length
        self.start = start
        self.end = end
        chip.AddWire(self)
        for n in chip.nodes:
            if n == self.start:
                n.AddOutput(self)
                #can be more efficient ig
        for e in self.end:
            for n in chip.nodes:
                if n == e:
                    n.AddInput(e)


#note: this program assumes all the required information is provided

#what this does: instantiates the components and adds them to stuff

    

    
        









    


