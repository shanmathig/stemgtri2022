from MST import MST
from Result import resulting_Nodes
def OldSteiner(Nodes):
    print("starting")
    Edges = MST(Nodes)
    
    #Compute current wire length
    Wire_Length_Initial = 0
    for i in range(len(Edges)):
        Wire_Length_Initial = Wire_Length_Initial + abs(Nodes[Edges[i][0]][0]-Nodes[Edges[i][1]][0]) + abs(Nodes[Edges[i][0]][1]-Nodes[Edges[i][1]][1])
    
    #Compute all possible additional points
    Temp_Positions = []
    Newnodes = []
    for i in range(len(Edges)):
        for j in range(len(Edges)):
            Temp_Positions = [Nodes[Edges[i][0]][0],Nodes[Edges[j][1]][1]]
            if Temp_Positions not in Newnodes:
                if Temp_Positions not in Nodes:
                    Newnodes.append(Temp_Positions)
            Temp_Positions = []
            Temp_Positions = [Nodes[Edges[j][1]][0],Nodes[Edges[i][0]][1]]
            Newnodes.append(Temp_Positions)
            if Temp_Positions not in Newnodes:
                if Temp_Positions not in Nodes:
                    Newnodes.append(Temp_Positions)
            Temp_Positions = []
    #Recalculate all possible MSTs with all extra possible points from the point pool we calculated (1 at a time)
    Temp_Positions = Nodes
    Wire_Length_Best=Wire_Length_Initial
    Best_Node = []
    Added_Nodes = []
    for l in range(len(Newnodes)):
        Best_Node = []   
        for i in range(len(Newnodes)):
            Temp_Positions.append(Newnodes[i])
            Wire_Length_Final = Eval(Temp_Positions)
            if(Wire_Length_Final<Wire_Length_Best):
                Wire_Length_Best=Wire_Length_Final
                Best_Node = Newnodes[i] 
                print(Newnodes[i])
            Temp_Positions.pop()
        if (Best_Node == []):
            resulting_Nodes(Temp_Positions)
            return Added_Nodes
        Temp_Positions.append(Best_Node)
        Added_Nodes.append(Best_Node)
    resulting_Nodes(Temp_Positions)
    return Added_Nodes
def Eval(Temp_Positions):
    New_Edges = MST(Temp_Positions)
    Wire_Length_Final = 0
    for j in range(len(New_Edges)): 
        Wire_Length_Final = Wire_Length_Final + abs(Temp_Positions[New_Edges[j][0]][0]-Temp_Positions[New_Edges[j][1]][0]) + abs(Temp_Positions[New_Edges[j][0]][1]-Temp_Positions[New_Edges[j][1]][1])
    return(Wire_Length_Final)
