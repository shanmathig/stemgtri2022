import math
from parserMC import parserMC
from pulp import *
import matplotlib.pyplot as plt
# Solve a multi-commodity flow problem.  Two products ('Pencils' and 

def Solver():
    m = LpProblem('solver',LpMinimize)
    network = ['n1','n2','n3','n4','n5','n6']
    Netconnects = [[0,11],[8,2],[3,5],[10,3],[6,7],[1,10]]
    Nodes = []
    XYpos = []
    Nodeletters = []
    values = parserMC()
    for i in range(len(values)):
        Nodes.append(i)
    for i in range(len(values)):
        Nodeletters.append(values[i][2])
    for i in range(len(values)):
        TempXY = [values[i][0]]
        TempXY.append(values[i][1])
        XYpos.append(TempXY)
    Objectivevars = []
    Tempvars = []
    Node_Edges = []
    finalnames = []
    Old_Edges = Edges(Nodes, XYpos)
    for i in range(len(Old_Edges)):
        Node_Edges.append(Old_Edges[i][:])
        Temp_Edges = Old_Edges[i]
        Temp_Edges.reverse()
        Node_Edges.append(Temp_Edges[:])
    Cost = Coster(Node_Edges, XYpos)
    for i in range(len(Cost)):
        for l in range(len(network)):
            Tempvars.append(LpVariable("X" + str(Nodeletters[Node_Edges[i][0]]) + str(Nodeletters[Node_Edges[i][1]])+ str(l+1),0,1,LpBinary))
        Objectivevars.append(Tempvars[:])
        Tempvars = []
    fakevars = []    
    for i in range(len(Cost)):
        for l in range(len(network)):
            Tempvars.append(Node_Edges[i])
        fakevars.append(Tempvars[:])
        Tempvars = []
    for i in range(len(Cost)):
        for l in range(len(network)):
            finalnames.append(str(l+1))
            Tempvars = []
    bigcost = []
    smallcost = []
    for i in range(len(Cost)):
        for l in range(len(network)):
            smallcost.append(Cost[i])
        bigcost.append(smallcost[:])
        smallcost = []
    m += lpSum(Objectivevars[i][u] * int(bigcost[i][u]) for i in range(len(Objectivevars)) for u in range(len(network)))
    #m.addConstr(Objectivevars[0-5] + Objectivevars[6-11] <=2)

    
    flatten_list = [element for sublist in fakevars for element in sublist]
    flatten_list2 = [element for sublist in Objectivevars for element in sublist]
    for k in range(len(Nodes)):
        
        seperatelist = []
        for i in range(len(Objectivevars)):
            Templist = []
            for l in range(len(network)):
                if(fakevars[i][l][0] == Nodes[k]):
                    Templist.append(Objectivevars[i][l])
                if(fakevars[i][l][1] == Nodes[k]):
                    Templist.append(Objectivevars[i][l])
            #print("templist=" + str(Templist))
            if Templist != []:
                seperatelist.append(Templist[:])
        negativelist = [1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1]
        Sourcelist = []
        for i in range(len(network)):
            if k == Netconnects[i][0]:
                Sourcelist.append(1)
            if k == Netconnects[i][1]:
                Sourcelist.append(-1)
            if k != Netconnects[i][0]:
                if k != Netconnects[i][1]:
                    Sourcelist.append(0)
        
        for n in range(len(network)):
            m += lpSum(seperatelist[f][n]*int(negativelist[f]) for f in range(int(len(seperatelist))))==Sourcelist[n]
            

    # m.setParam('Cuts', 0)
    # m.setParam('Heuristics', 0)
    # m.setParam('Presolve' ,0)
    # m.setParam('Method', 1)
    Templist = []
    Newlist = []
    for i in range(int(len(Objectivevars))):
        if(i%2 == 0):
            Templist.append(Objectivevars[i])
        if(i%2 != 0):
            Templist.append(Objectivevars[i])
            Newlist.append(Templist)
            Templist = []
    

    for i in range(len(Newlist)):

        m += lpSum(Newlist[i][k][l] for l in range(len(network)) for k in range(2)) <= 4
    m.solve()
    printlist = []
    if m.status == GRB.status.OPTIMAL:
        for i in range(len(flatten_list)):
            if abs(m.x[i]) == 1:
                printlist.append([flatten_list[i], int(finalnames[i])])
    finallist = []
    for l in range(len(network)):
        for i in range(len(printlist)):
            if(printlist[i][1] == l+1):
                finallist.append(printlist[i])
    for i in range(len(finallist)):
        print(str(Nodeletters[finallist[i][0][0]])+" -- "+str(Nodeletters[finallist[i][0][1]])+ " net:"+ str(finallist[i][1]))
    print(m.getParamInfo)
    print (m.display())
    m.write('model.lp')
    # m.computeIIS() 
    # print(m.IISConstr)
    # m.feasRelaxS(0, False, False, True) 
    # m.optimize()

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