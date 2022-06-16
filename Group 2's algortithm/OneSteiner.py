import math
import itertools as it
from datetime import datetime
def OneSteiner(Nodes, Edges):
    
    #Compute current wire length
    wli = 0
    for i in range(len(Edges)):
        wli = wli + math.dist(Nodes[Edges[i][0]],Nodes[Edges[i][1]])
    print("Initial wirelength"+ str(wli))
    #Compute all possible additional points
    positionsub = []
    Newnodes = []
    for i in range(len(Edges)):
        pnt1 = Edges[i][0]
        pnt2 = Edges[i][1]
        lpnt1 = Nodes[pnt1]
        lpnt2 = Nodes[pnt2]
        print(lpnt1)
        print(lpnt2)
        lpnt1x = lpnt1[0]
        lpnt1y = lpnt1[1]
        lpnt2x = lpnt2[0]
        lpnt2y = lpnt2[1]
        positionsub = [lpnt1x,lpnt2y]
        if positionsub not in Newnodes:
            Newnodes.append(positionsub)
        positionsub = []
        positionsub = [lpnt2x,lpnt1y]
        Newnodes.append(positionsub)
        if positionsub not in Newnodes:
            Newnodes.append(positionsub)
        positionsub = []
    print("New possible nodes" + str(Newnodes))
    #Recalculate all possible MSLs with 1 extra possible point from the point pool we calculated
    Nodesub2 = []
    Nodessub = Nodes
    wlb=wli
    bestnode = []
    start = datetime.now()
    for i in range(len(Newnodes)):
        Nodessub.append(Newnodes[i])
        newedges = MST2(Nodessub)

        wlf = 0
        for j in range(len(newedges)): 
            wlf = wlf + math.dist(Nodessub[newedges[j][0]],Nodessub[newedges[j][1]])

        if(wlf<wlb):
            wlb=wlf
            bestnode = [Newnodes[i]]
        Nodessub.pop()
    for i in range(len(Newnodes)):
        Nodessub.append(Newnodes[i])
        for k in range(len(Newnodes)):
            Nodessub.append(Newnodes[k])
            newedges = MST2(Nodessub)

            wlf = 0
            for j in range(len(newedges)): 
                wlf = wlf + math.dist(Nodessub[newedges[j][0]],Nodessub[newedges[j][1]])

            if(wlf<wlb):
                wlb=wlf
                bestnode = [Newnodes[i]]+[Newnodes[k]]
            Nodessub.pop()
        Nodessub.pop()
    for i in range(len(Newnodes)):
        Nodessub.append(Newnodes[i])
        for k in range(len(Newnodes)):
            Nodessub.append(Newnodes[k])
            for l in range(len(Newnodes)):
                Nodessub.append(Newnodes[l])
                newedges = MST2(Nodessub)

                wlf = 0
                for j in range(len(newedges)): 
                    wlf = wlf + math.dist(Nodessub[newedges[j][0]],Nodessub[newedges[j][1]])

                if(wlf<wlb):
                    wlb=wlf
                    bestnode = [Newnodes[i]]+[Newnodes[k]]+[Newnodes[l]]
                Nodessub.pop()
            Nodessub.pop()
        Nodessub.pop()
    for o in range(len(Newnodes)):
        Nodessub.append(Newnodes[o])
        for i in range(len(Newnodes)):
            Nodessub.append(Newnodes[i])
            for k in range(len(Newnodes)):
                Nodessub.append(Newnodes[k])
                for l in range(len(Newnodes)):
                    Nodessub.append(Newnodes[l])
                    newedges = MST2(Nodessub)

                    wlf = 0
                    for j in range(len(newedges)): 
                        wlf = wlf + math.dist(Nodessub[newedges[j][0]],Nodessub[newedges[j][1]])

                    
                    if(wlf<wlb):
                        wlb=wlf
                        bestnode = [Newnodes[i]]+[Newnodes[k]]+[Newnodes[l]]+[Newnodes[o]]
                    Nodessub.pop()
                Nodessub.pop()
            Nodessub.pop()
        Nodessub.pop()
    for u in range(len(Newnodes)):
        Nodessub.append(Newnodes[u])
        for o in range(len(Newnodes)):
            Nodessub.append(Newnodes[o])
            for i in range(len(Newnodes)):
                Nodessub.append(Newnodes[i])
                for k in range(len(Newnodes)):
                    Nodessub.append(Newnodes[k])
                    for l in range(len(Newnodes)):
                        Nodessub.append(Newnodes[l])
                        newedges = MST2(Nodessub)
                        wlf = 0
                        for j in range(len(newedges)): 
                            wlf = wlf + math.dist(Nodessub[newedges[j][0]],Nodessub[newedges[j][1]])
                        
                        if(wlf<wlb):
                            wlb=wlf
                            bestnode = [Newnodes[i]]+[Newnodes[k]]+[Newnodes[l]]+[Newnodes[o]]+[Newnodes[u]]
                        Nodessub.pop()
                    Nodessub.pop()
                Nodessub.pop()
            Nodessub.pop()
        Nodessub.pop()
    print("best addition node(s) is "+ str(bestnode) +" at a wirelength of "+ str(wlb))
    Nodesub2 = Nodes + bestnode
    print(Nodesub2)
    newedges2 = MST2(Nodesub2)
    print(newedges2)
    end = datetime.now()
    print(str(end-start))
    return()
def MST2(input):
    positions = []
    positionsub2 =[]
    for i in range(len(input)):
        for l in range(len(input)):
            positionsub2.append(math.dist(input[i], input[l]))
        positions.append(positionsub2)
        positionsub2 = []
    vertecies = len(input)
    INF=9999
    selected_node = []
    for i in range(len(input)):
        selected_node.append(0)
    no_edge = 0
    selected_node[0] = True
    # printing for edge and weight
    newedges = []
    sublist = []
    while (no_edge < vertecies - 1):
        minimum = INF
        a = 0
        b = 0
        for m in range(vertecies):
           if selected_node[m]:
               for n in range(vertecies):
                  if ((not selected_node[n]) and positions[m][n]):  
                        # not in selected and there is an edge
                        if minimum > positions[m][n]:
                            minimum = positions[m][n]
                            a = m
                            b = n
        #prints output between the best edges to draw between all the nodes + the weight of the edge drawn between the two (0-4:5 would be an edge between node 0 and 4 with a weight of 5)
        sublist.append(a)
        sublist.append(b)
        newedges.append(sublist)
        sublist=[]
        selected_node[b] = True
        no_edge += 1
    return newedges