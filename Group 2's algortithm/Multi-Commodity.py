import math
from tempfile import tempdir
from parserMC import parserMC
from gurobipy import *
# Solve a multi-commodity flow problem.  Two products ('Pencils' and 

def Solver():
    m = Model('solver')
    network = ['n1','n2','n3','n4','n5','n6']
    Netconnects = [[0,11],[8,2],[3,5],[10,3],[6,7],[1,10]]
    Nodes = []
    XYpos = []
    values = parserMC()
    for i in range(len(values)):
        Nodes.append(i)
    for i in range(len(values)):
        TempXY = [values[i][0]]
        TempXY.append(values[i][1])
        XYpos.append(TempXY)
    Objectivevars = []
    Node_Edges = Edges(Nodes, XYpos)
    Cost = Coster(Node_Edges, XYpos)
    for i in range(len(Cost)):
        for l in range(len(network)):
            Objectivevars.append(m.addVar(vtype=GRB.BINARY, name = str(Node_Edges[i]) + " n" + str(l+1)))
    m.update()
    print(Objectivevars)
    bigcost = []
    for i in range(len(Cost)):
        for l in range(len(network)):
            bigcost.append(Cost[i])
    for i in range(len(Objectivevars)):
        print("\nEdge =" + str(Objectivevars[i]) + str(bigcost[i]))
    m.setObjective(quicksum(Objectivevars[i] * bigcost[i] for i in range(len(Objectivevars))), GRB.MINIMIZE)
    m.addConstr()     
    m.optimize()
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
            print(XYpos[l])
            print(XYpos[i])
            X_Difference = XYpos[l][0]-XYpos[i][0]
            Y_Difference = XYpos[l][1]-XYpos[i][1]
            if(XYpos[l][1] == XYpos[i][1]):
                if(Nodes[l]!=Nodes[i]):
                    if(X_Difference > 0):
                        print([Nodes[l],Nodes[i]])
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