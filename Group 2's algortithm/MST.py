def MST(Nodes):
    Rect_Dist_Matrix = []
    Temp_Dist =[]
    for i in range(len(Nodes)):
        for l in range(len(Nodes)):
            rect_distance = abs(Nodes[i][0]-Nodes[l][0]) + abs(Nodes[i][1]-Nodes[l][1])
            Temp_Dist.append(rect_distance)
        Rect_Dist_Matrix.append(Temp_Dist)
        Temp_Dist = []
    Vertex_Count = len(Nodes)
    INF=999999
    Selected_Node = []
    for i in range(len(Nodes)):
        Selected_Node.append(0)
    No_Edge = 0
    Selected_Node[0] = True
    # printing for edge and weight
    Final_Edges = []
    Temp_Edges = []
    while (No_Edge < Vertex_Count - 1):
        minimum = INF
        a = 0
        b = 0
        for m in range(Vertex_Count):
           if Selected_Node[m]:
               for n in range(Vertex_Count):
                  if ((not Selected_Node[n]) and Rect_Dist_Matrix[m][n]):  
                        # not in selected and there is an edge
                        if minimum > Rect_Dist_Matrix[m][n]:
                            minimum = Rect_Dist_Matrix[m][n]
                            a = m
                            b = n
        #prints output between the best edges to draw between all the nodes + the weight of the edge drawn between the two (0-4:5 would be an edge between node 0 and 4 with a weight of 5)
        Temp_Edges.append(a)
        Temp_Edges.append(b)
        Final_Edges.append(Temp_Edges)
        Temp_Edges=[]
        Selected_Node[b] = True
        No_Edge += 1

    return Final_Edges
