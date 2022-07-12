import math
from parserMC import parserMC
from gurobipy import *
#This code uses no classes, started with lots of them and progressively regressed to lists trying to fix LP solver
def Solver():
    #Make the model
    m = Model('solver')
    #Networks
    Networks = ['n1','n2','n3','n4','n5','n6']
    #Connections between nodes on networks in ascending order
    Network_Connections = [[0,11],[8,2],[3,5],[10,3],[6,7],[1,10]]
    #Creates a list of nodes (int, eg [1,2,3,4])
    #Creates a list of nodes (letter, eg [a,b,c,d])
    #Creates a list of positions in XY ([[x1,y1],[x2,y2]])
    Parsed_Nodes = parserMC()
    Nodes_XY = []
    Node_Letters = []
    Node_Numbers = []
    for i in range(len(Parsed_Nodes)):
        Temporary_XY = [Parsed_Nodes[i][0]]
        Temporary_XY.append(Parsed_Nodes[i][1])
        Nodes_XY.append(Temporary_XY)
        Node_Letters.append(Parsed_Nodes[i][2])
        Node_Numbers.append(i)
    #Returns all edges ([[0,1],[1,0]])
    All_Edges = []
    Inital_Edges = Edges(Node_Numbers, Nodes_XY)
    for i in range(len(Inital_Edges)):
        All_Edges.append(Inital_Edges[i][:])
        Temporary_Edges = Inital_Edges[i]
        Temporary_Edges.reverse()
        All_Edges.append(Temporary_Edges[:])
    #Returns the "cost" (distance)
    Cost = Coster(All_Edges, Nodes_XY)
    #Assigns all variables in objective function, nested by network ([[[Xab1],[Xab2]],[[Xba1],[Xba2]]])
    Objective_Vars = []
    Temporary_Vars = []
    for i in range(len(Cost)):
        for l in range(len(Networks)):
            Temporary_Vars.append(m.addVar(vtype=GRB.BINARY, name = "X" + str(Node_Letters[All_Edges[i][0]]) + str(Node_Letters[All_Edges[i][1]])+ str(l+1)))
        Objective_Vars.append(Temporary_Vars[:])
        Temporary_Vars = []
    #Update Gurobi
    m.update()
    #Creates a list of costs in the same format as the objective function
    Edge_Costs = []
    for i in range(len(Cost)):
        for l in range(len(Networks)):
            Temporary_Vars.append(Cost[i])
        Edge_Costs.append(Temporary_Vars[:])
        Temporary_Vars = []
    #Set the objective function
    m.setObjective(quicksum(Objective_Vars[i][u] * int(Edge_Costs[i][u]) for i in range(len(Objective_Vars)) for u in range(len(Networks))), GRB.MINIMIZE)
    #Creates variables in the same format as objective variables, but with ints so they can be compared
    StandIn_Vars = []
    for i in range(len(Cost)):
        for l in range(len(Networks)):
            Temporary_Vars.append(All_Edges[i])
        StandIn_Vars.append(Temporary_Vars[:])
        Temporary_Vars = []
    for k in range(len(Node_Numbers)):
        #Seperates list into networks
        Seperated_List = []
        for i in range(len(Objective_Vars)):
            Templist = []
            Templist2 = []
            for l in range(len(Networks)):
                if(StandIn_Vars[i][l][0] == Node_Numbers[k]):
                    Templist.append(Objective_Vars[i][l])
                    Templist2.append(StandIn_Vars[i][l])
            Templist4 = []
            if Templist != []:
                Templist3 = Templist2[0][:]
                Templist3.reverse()
                for o in range(len(Objective_Vars)):
                    for h in range(len(Networks)):
                        if StandIn_Vars[o][h] == Templist3:
                            Templist4.append(Objective_Vars[o][h])
                Seperated_List.append(Templist[:])
                Seperated_List.append(Templist4)
        #Create an index of which equations should be set to -1, 0, and 1
        RH_Index = []
        for i in range(len(Networks)):
            if k == Network_Connections[i][0]:
                RH_Index.append(1)
            if k == Network_Connections[i][1]:
                RH_Index.append(-1)
            if k != Network_Connections[i][0]:
                if k != Network_Connections[i][1]:
                    RH_Index.append(0)
        #Pattern to set variables coefficient (1 or -1) in the first constraint equation
        Negative_Index = [1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1]
        #Set the first set of contraint equations (xab1 - xba1 = 0)
        print(Seperated_List)
        
        for n in range(len(Networks)):
            m.addConstr(quicksum(Seperated_List[f][n]*int(Negative_Index[f]) for f in range(int(len(Seperated_List))))==RH_Index[n])
    #Creates a formatted list of the objective vars for use in the last set of contraints
    Formatted_Vars = []
    for i in range(int(len(Objective_Vars))):
        if(i%2 == 0):
            Temporary_Vars.append(Objective_Vars[i])
        if(i%2 != 0):
            Temporary_Vars.append(Objective_Vars[i])
            Formatted_Vars.append(Temporary_Vars)
            Temporary_Vars = []
    #Creates the last contraint, 3 should be 2 for the book problem but that makes it unfeasible
    for i in range(len(Formatted_Vars)):
        m.addConstr(quicksum(Formatted_Vars[i][k][l] for l in range(len(Networks)) for k in range(2)) <= 2)
    #Run the optimizer
    #m.setParam('PoolSolutions',50)
    #m.setParam('PoolSearchMode',2)
    m.optimize()
    #Prints the result
    Print_Names = []
    Final_Names = []
    for i in range(len(Cost)):
        for l in range(len(Networks)):
            Final_Names.append(str(l+1))
    Flattened_List = [i for m in StandIn_Vars for i in m]
    if m.status == GRB.status.OPTIMAL:
        for i in range(len(Flattened_List)):
            if abs(m.x[i]) == 1:
                Print_Names.append([Flattened_List[i], int(Final_Names[i])])
    Final_Nodes = []
    for l in range(len(Networks)):
        for i in range(len(Print_Names)):
            if(Print_Names[i][1] == l+1):
                Final_Nodes.append(Print_Names[i])
    for i in range(len(Final_Nodes)):
        print(str(Node_Letters[Final_Nodes[i][0][0]])+" -- "+str(Node_Letters[Final_Nodes[i][0][1]])+ " net:"+ str(Final_Nodes[i][1]))

def Coster(Edges, XYpos):
    Costlist = []
    for i in range(len(Edges)):
        Costlist.append(math.dist(XYpos[Edges[i][0]],XYpos[Edges[i][1]]))
    return(Costlist)
def Edges(Nodes, XYpos):
    Weightlist = []
    XPoslist = []
    XNeglist = []
    YPoslist = []
    YNeglist = []
    for l in range(len(XYpos)):
        PosbestX = 999
        Negbestx = 999
        PosbestY = 999
        NegbestY = 999
        for i in range(len(XYpos)):
            X_Difference = XYpos[l][0]-XYpos[i][0]
            Y_Difference = XYpos[l][1]-XYpos[i][1]
            if(XYpos[l][1] == XYpos[i][1]):
                if(Nodes[l]!=Nodes[i]):
                    if(X_Difference > 0):
                        if(X_Difference < PosbestX):
                            
                            XPoslist = [Nodes[l],Nodes[i]]
                            PosbestX = X_Difference
                    if(X_Difference < 0):
                        if(X_Difference > Negbestx):
                            XNeglsit = [Nodes[l],Nodes[i]]
                            Negbestx = X_Difference
            if(XYpos[l][0] == XYpos[i][0]):
                if(Nodes[l]!=Nodes[i]):
                    if(Y_Difference > 0):
                        if(Y_Difference < PosbestY):
                            YPoslist = [Nodes[l],Nodes[i]]
                            PosbestY = Y_Difference
                    if(Y_Difference < 0):
                        if(Y_Difference > NegbestY):
                            YNeglsit = [Nodes[l],Nodes[i]]
                            NegbestY = Y_Difference        
        if(XPoslist != []):
            if XPoslist not in Weightlist:
                Weightlist.append(XPoslist)
        if(XNeglist != []):
            if XNeglist not in Weightlist:
                Weightlist.append(XNeglist)
        if(YPoslist != []):
            if YPoslist not in Weightlist:
                Weightlist.append(YPoslist)
        if(YNeglist != []):
            if YNeglist not in Weightlist:
                Weightlist.append(YNeglist)
    return(Weightlist)

Solver()