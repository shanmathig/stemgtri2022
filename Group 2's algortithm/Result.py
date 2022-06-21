from MST import MST
def resulting_Nodes(Final_Nodes):
    Newedges = MST(Final_Nodes)
    for i in range(len(Newedges)):
        First_xy = Final_Nodes[Newedges[i][0]]
        Second_xy = Final_Nodes[Newedges[i][1]]
    Wire_Length_Final = 0
    for i in range(len(Newedges)):
        Wire_Length_Final = Wire_Length_Final + abs(Final_Nodes[Newedges[i][0]][0]-Final_Nodes[Newedges[i][1]][0]) + abs(Final_Nodes[Newedges[i][0]][1]-Final_Nodes[Newedges[i][1]][1])
    return Final_Nodes