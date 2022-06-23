from MST import MST
from Result import resulting_Nodes
import time
def OneSteiner(Nodes):
    start_time = time.time()
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
            if Temp_Positions not in Newnodes:
                if Temp_Positions not in Nodes:
                    Newnodes.append(Temp_Positions)
            Temp_Positions = []
    print("starting")
    
    #Divide up the points among the threads
    data = thread(Nodes,Newnodes,Newnodes)
    Best_Nodes_Final = []
    print("DATA HERE DUMMY:"+ str(data))
    Wire_Length_Best = Wire_Length_Initial
    for i in range(len(data)):
        Wire_Length_Current = Eval(data[i])
        if(Wire_Length_Current < Wire_Length_Best):
            Wire_Length_Best = Wire_Length_Current
            Best_Nodes_Final = data[i]
            #print(Best_Nodes_Final)
            #print(Wire_Length_Best)
    resulting_Nodes(Best_Nodes_Final)
    for i in range(len(Nodes)):
        Best_Nodes_Final.remove(Nodes[i])
    print(time.time()-start_time)
    return(Best_Nodes_Final)

def thread(Nodes, Newnodes, Trynodes):
    Best_Nodes_Current = BestNodes(Nodes, Trynodes)
    #print("bestnodesCurrent"+ str(Best_Nodes_Current))
    Nodes_List = [Nodes]
    k=0
    while(True):
        try:
            #print("RUN LENGTH HERE:"+ str(k))
            
            Best_Nodes = BestNodes(Nodes_List[k], Best_Nodes_Current)
            Nodes_Standin = Nodes_List[k]
            #print(Best_Nodes)
            for i in range(len(Best_Nodes)):
                
                Nodes_Standin.append(Best_Nodes[i][:])
                #print("Trying:" + str(Nodes_Standin))
                Nodes_List.append(Nodes_Standin[:])
                #print(Nodes_List)
                #print("Best_Nodes:" + str(Best_Nodes[i]))
                
                Best_Nodes_List = BestNodes(Nodes_Standin, Newnodes)
                #print("Best_Nodes_List" + str(Best_Nodes_List))
                if(Best_Nodes != []):
                    for m in range(len(Best_Nodes_List)):
                        Nodes_Standin.append(Best_Nodes_List[m][:])
                        #print("nodes_standin:" + str(Nodes_Standin))
                        if(Nodes_Standin not in Nodes_List):
                            Nodes_List.append(Nodes_Standin[:])
                        #print("NodesSTANDINHERE1:" + str(Nodes_Standin))
                        #print("Nodes_List:" + str(Nodes_List))
                        Nodes_Standin.pop()
                        #print("NodesSTANDINHERE2:" + str(Nodes_Standin))
                Nodes_Standin.pop()
                
            k=k+1

        except IndexError:
            return(Nodes_List)
        
def Eval(Temp_Positions):
    New_Edges = MST(Temp_Positions)
    Wire_Length_Final = 0
    for j in range(len(New_Edges)): 
        Wire_Length_Final = Wire_Length_Final + abs(Temp_Positions[New_Edges[j][0]][0]-Temp_Positions[New_Edges[j][1]][0]) + abs(Temp_Positions[New_Edges[j][0]][1]-Temp_Positions[New_Edges[j][1]][1])
    return(Wire_Length_Final)

def BestNodes(Oldnodes, Newnodes):
    #print(Oldnodes)
    #print(Newnodes)
    Best_Nodes = []
    Wire_Length_Initial = Eval(Oldnodes)
    for i in range(len(Newnodes)):
        Oldnodes.append(Newnodes[i])
        if(Eval(Oldnodes) < Wire_Length_Initial):
            if(Newnodes[i] not in Best_Nodes):
                Best_Nodes.append(Newnodes[i])
        Oldnodes.pop()
        #print(Best_Nodes)
    return Best_Nodes
def BestNodes1(Oldnodes, Newnodes):
    Best_Nodes = []
    Wire_Length_Initial = Eval(Oldnodes)
    Oldnodes.append(Newnodes)
    if(Eval(Oldnodes) < Wire_Length_Initial):
        if(Newnodes not in Best_Nodes):
            Best_Nodes.append(Newnodes)
    Oldnodes.pop()
        #print(Best_Nodes)
    return Best_Nodes
        

