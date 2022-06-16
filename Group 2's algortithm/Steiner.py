
def MSL(positions):
    vertecies = len(positions)
    INF=999999
    selected_node = []
    for i in range(len(positions)):
        selected_node.append(0)
    no_edge = 0
    selected_node[0] = True
    # printing for edge and weight
    print("Edge : Weight\n")
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
        print(str(a) + "-" + str(b) + ":" + str(positions[a][b]))
        selected_node[b] = True
        no_edge += 1