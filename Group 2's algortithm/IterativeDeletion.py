from LSteiner import *
from MST import MST
import math

#rn just pseudo code and stuff

class Net:
    #grid is really only used for setting up a structure to put points in
    grid : Grid
    cellwidth : int
    cellheight : int
    cells : list
    edges : list

    def __init__(self,g,cw,ch):
        self.grid = g
        self.cellwidth = cw
        self.cellheight = ch
        self.cells = []
        self.edges = []

    def addcell(x,y):
        pass
    
    def netConnectionGraph(self):
        pass

class Cell:
    x : int
    y : int
    #x2 is the point at the top of the cell
    x2 : int
    connectededgestop : list
    connectededgesbottom : list
    def __init__(self,x,y,x2):
        self.x = x
        self.y = y
        self.x2 = x2
        self.connectededgestop = []
        self.connectededgesbottom = []
    def addedgetop(self,edge):
        self.connectededgestop.append(edge)

#An edge connects 2 cells
class Edge:
    cells : list
    #pass 2 Cell objects as parameters

    
    def __init__(self,c1,c2):
        self.cells = [c1,c2]
        c1.addedge(self)
        c2.addedge(self)

    

t = Net(Grid(21,21),2,3)


