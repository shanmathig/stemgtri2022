import math
from operator import truediv
from time import sleep
from matplotlib.pyplot import connect
import MST
import parser

emptychar = "."
pointchar = "o"
maxval = 2147483647
class Point:
    xVal : int
    yVal : int
    def __init__(self,xVal,yVal):
        self.xVal = xVal
        self.yVal = yVal
    
    def PrintPoint(self):
        print("("+str(self.xVal)+","+str(self.yVal)+")")

    def DiffX(self,other):
        return math.fabs(self.xVal-other.xVal)
    
    def DiffY(self,other):
        return math.fabs(self.yVal-other.xVal)

    def GetWireLength(self,other):
        return self.DiffX(other) + self.DiffY(other)

    #only used for the get closest three function
    def GetWireLengthAndPoint(self,other):
        return {'wirelength' : self.DiffX(other) + self.DiffY(other),'point' : other}

    #to compare two points
    def equals(self,other):
        if self.xVal == other.xVal and self.yVal == other.yVal:
            return True
        return False
class Wire:
    start : Point
    end : Point
    bend : Point
    ends : list
    def __init__(self,p1,p2,grid):
        self.start = p1
        self.end = p2
        self.ends = [p1,p2]
        self.bend = Point(p1.xVal,p2.yVal)
        grid.wires.append(self)

    #changes the bend
    def changeBend(self):
        if self.bend == Point(self.start.xVal,self.end.yVal):
            self.bend = Point(self.end.xVal,self.start.yVal)
        elif self.bend == Point(self.end.xVal,self.start.yVal):
            self.bend = Point(self.start.xVal,self.end.yVal)
    
    def wequals(self,other):
        if self.start.equals(other.start) and self.end.equals(other.end) and self.bend.equals(other.end):
            return True
        return False
    def PrintWire(self):
        print("start") 
        self.start.PrintPoint()
        print("end")
        self.end.PrintPoint()
        print("bend")
        self.bend.PrintPoint()
        print("~~~~~~~~~~~~~~~")

class Grid:
    grid : list
    points : list
    wires : list
    #makes an empty grid
    def __init__(self,xLen,yLen):
        self.grid = []
        self.points = []
        self.wires = []
        for i in range(yLen):
            self.grid.append([])
            for j in range(xLen):
                self.grid[i].append(emptychar)
    
    #sets a point on the grid, to indicate that there is a point there
    def Enable(self,x,y):
        self.grid[y][x] = pointchar
        #self.PrintNeatly()
    
    
    #def Enable(self,pt):
        #pass
    #prints the graph
    def PrintGraph(self):
        for index,value in enumerate(self.grid):
            a = ""
            for j in value:
                a += (str(j) + " ")
            print(a)
    
    #Updates the database of points, sorted by left to right
    def UpdatePoints(self):
        self.points = []
        for x in range(len(self.grid[0])):
            for yn,y in enumerate(self.grid):
                if y[x] == pointchar:
                    self.points.append(Point(x,yn))

    #Prints out the list of points
    def PrintPointList(self):
        for p in self.points:
            p.PrintPoint()
    def PrintWireList(self):
        for i,p in enumerate(self.wires):
            print(i)
            p.PrintWire()
    

            

    #now for the big stuff
    def Lsteiner(self):

        # space is saved whenever the bend point is inside one of the other wires (between another bend point and 
        # either the start or end point of the first wire)
        # find out which bending saves more space
        
        for value in self.wires:
            connectedwires = []
            for p in value.ends:
                for w in self.wires:
                    for wp in w.ends:
                        if wp.equals(p) and not(w.wequals(value)):
                            connectedwires.append(w)
            for c in connectedwires:
                #if not ((value.bend.xVal == c.bend.xVal) and ((value.bend.yVal <= value.start.yVal and value.bend.yVal >= value.end.yVal) or (value.bend.yVal <= value.end.yVal and value.bend.yVal >= value.start.yVal))) or ((value.bend.yVal == c.bend.yVal) and ((value.bend.xVal <= value.start.xVal and value.bend.xVal >= value.end.xVal) or (value.bend.xVal <= value.end.xVal and value.bend.xVal >= value.start.xVal))):
                value.changeBend()
                if not ((value.bend.xVal == c.bend.xVal) and ((value.bend.yVal <= value.start.yVal and value.bend.yVal >= value.end.yVal) or (value.bend.yVal <= value.end.yVal and value.bend.yVal >= value.start.yVal))) or ((value.bend.yVal == c.bend.yVal) and ((value.bend.xVal <= value.start.xVal and value.bend.xVal >= value.end.xVal) or (value.bend.xVal <= value.end.xVal and value.bend.xVal >= value.start.xVal))):
                    value.changeBend()



def convertlist(pts):
    ptlist = []
    for i in pts:
        ptlist.append([i.xVal,i.yVal])
    return ptlist

def wiremaker(ptarr,mstlist,grid):
    for ptpairs in mstlist:
        Wire(Point(ptarr[ptpairs[0]][0],ptarr[ptpairs[0]][1]),Point(ptarr[ptpairs[1]][0],ptarr[ptpairs[1]][1]),grid)
        

#points
g = Grid(11,11)
g.Enable(1,5)
g.Enable(4,4)
g.Enable(2,8)
g.Enable(3,7)
g.Enable(5,9)
g.Enable(7,5)
g.Enable(8,2)
g.Enable(10,2)
g.Enable(10,10)
g.PrintGraph()
g.UpdatePoints()
#g.PrintPointList()
print(convertlist(g.points))
print(MST.MST(convertlist(g.points)))

g.PrintWireList()
g.Lsteiner()
g.PrintWireList()
wiremaker(convertlist(g.points),MST.MST(convertlist(g.points)),g)
g.PrintWireList()
g.Lsteiner()
g.PrintWireList()
#print (parser.parser())