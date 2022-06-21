from MST import MST
from Result import resulting_Nodes
def OneSteiner(Nodes):
    Edges = MST(Nodes)
    #Compute current wire length
    Wire_Length_Initial = 0
    for i in range(len(Edges)):
        Wire_Length_Initial = Wire_Length_Initial + abs(Nodes[Edges[i][0]][0]-Nodes[Edges[i][1]][0]) + abs(Nodes[Edges[i][0]][1]-Nodes[Edges[i][1]][1])
    print("Initial wirelength: "+ str(Wire_Length_Initial))
    print("Initial routing: " + str(Edges))
    #Compute all possible additional points
    Temp_Positions = []
    Newnodes = []
    for i in range(len(Edges)):
        for j in range(len(Edges)):
            First_Point_x = Nodes[Edges[i][0]][0]
            First_Point_y = Nodes[Edges[i][0]][1]
            Second_Point_x = Nodes[Edges[j][1]][0]
            Second_Point_y = Nodes[Edges[j][1]][1]
            Temp_Positions = [First_Point_x,Second_Point_y]
            if Temp_Positions not in Newnodes:
                Newnodes.append(Temp_Positions)
            Temp_Positions = []
            Temp_Positions = [Second_Point_x,First_Point_y]
            Newnodes.append(Temp_Positions)
            if Temp_Positions not in Newnodes:
                if Temp_Positions not in Nodes:
                    Newnodes.append(Temp_Positions)
            Temp_Positions = []
    print("New possible nodes" + str(Newnodes))
    #Recalculate all possible MSLs with 1 extra possible point from the point pool we calculated
    Temp_Positions = Nodes
    Wire_Length_Best=Wire_Length_Initial
    Best_Node = []
    for l in range(len(Newnodes)):
        Best_Node = []   
        for i in range(len(Newnodes)):
            Temp_Positions.append(Newnodes[i])
            New_Edges = MST(Temp_Positions)
            Wire_Length_Final = 0
            for j in range(len(New_Edges)): 
                Wire_Length_Final = Wire_Length_Final + abs(Temp_Positions[New_Edges[j][0]][0]-Temp_Positions[New_Edges[j][1]][0]) + abs(Temp_Positions[New_Edges[j][0]][1]-Temp_Positions[New_Edges[j][1]][1])
            if(Wire_Length_Final<Wire_Length_Best):
                Wire_Length_Best=Wire_Length_Final
                Best_Node = Newnodes[i]
            Temp_Positions.pop()
        print(str(Best_Node))
        if (Best_Node == []):
            Output = resulting_Nodes(Temp_Positions)
            return Output
        Temp_Positions.append(Best_Node)
    Output = resulting_Nodes(Temp_Positions)
    return Output
