"""
HOW TO USE

Import everything

Classes:
Point(int x, int y)
Wire(Point start, Point end, Grid grid)
Grid(int xlength, int ylength) because of the way lists work in python and coding in general, add one to each length,
for example if you wanted to make a 4x5 grid you would instantiate it as Grid(5,6)

Important Methods:

Part of the Grid class:
Enable(int x,int y) : enables a point on the grid. You should use UpdatePoints() right after to add the points to the grid's point list
UpdatePoints() : Iterates through the grid and adds all enabled points to the point list
(mainly used for debugging)
PrintGraph() : prints out the graph
PrintPointList() : prints out all the points on the graph
PrintWireList() : Prints out the start, end, and bend points of each wire
Lsteiner() : Runs the LSteiner algorithm on a grid with wires and nodes 

Not Part Of A Class:
convertlist(list points) : converts a list of Point objects into a nested array
wiremaker(list points, list mst, list grid) : takes a list of points and MST wiring and places the wires on the grid
convertwirebendstonodes(Grid grid) : takes all the wires of the grid and turns their bend points into a nested array


"""




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
        if self.bend.equals(Point(self.start.xVal,self.end.yVal)):
            self.bend = Point(self.end.xVal,self.start.yVal)
        elif self.bend.equals(Point(self.end.xVal,self.start.yVal)):
            self.bend = Point(self.start.xVal,self.end.yVal)
    
    def wequals(self,other):
        if self.start.equals(other.start) and self.end.equals(other.end): # and self.bend.equals(other.end):
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
    
    def findPotentialOverlap(self,other):
        mutualPoint = ""
        for i in self.ends:
            for j in other.ends:
                if i.equals(j):
                    mutualPoint = i
                    #mutualPoint.PrintPoint()
        
        #returns 0 if no mutual point
        if mutualPoint == "":
            return 0

        if mutualPoint.xVal == self.bend.xVal:
            flipped = False
            if not mutualPoint.xVal == other.bend.xVal:
                other.changeBend()
                flipped = True
                if not mutualPoint.xVal == other.bend.xVal:
                    other.changeBend()
                    return 0
            
            sb = abs(self.bend.yVal - mutualPoint.yVal)
            ob = abs(other.bend.yVal - mutualPoint.yVal)
            sb2 = self.bend.xVal - mutualPoint.xVal
            ob2 = other.bend.xVal - mutualPoint.xVal
            if sb2 * ob2 < 0:
                return 0
            if sb > ob:
                if flipped:
                    other.changeBend()
                return ob
            elif sb < ob:
                if flipped:
                    other.changeBend()
                return sb
                
            else:
                if flipped:
                    other.changeBend()
                return sb
        elif mutualPoint.yVal == self.bend.yVal:
            flipped = False
            if not mutualPoint.yVal == other.end.yVal:
                other.changeBend()
                flipped = True
                if not mutualPoint.yVal == other.bend.yVal:
                    other.changeBend()
                    return 0
            
            sb = abs(self.bend.xVal - mutualPoint.xVal)
            ob = abs(other.bend.xVal - mutualPoint.xVal)
            sb2 = self.bend.xVal - mutualPoint.xVal
            ob2 = other.bend.xVal - mutualPoint.xVal
            if sb2 * ob2 < 0:
                return 0
            if sb > ob:
                if flipped:
                    other.changeBend()
                return ob
            elif sb < ob:
                if flipped:
                    other.changeBend()
                return sb
                
            else:
                if flipped:
                    other.changeBend()
                return sb
        else:
            return 0

    def findOverlap(self,other):
        mutualPoint = ""
        for i in self.ends:
            for j in other.ends:
                if i.equals(j):
                    mutualPoint = i
                    mutualPoint.PrintPoint()
        
        #returns 0 if no mutual point
        if mutualPoint == "":
            return 0

        if mutualPoint.xVal == self.bend.xVal:
            
            
            sb = abs(self.bend.yVal - mutualPoint.yVal)
            ob = abs(other.bend.yVal - mutualPoint.yVal)
            sb2 = self.bend.xVal - mutualPoint.xVal
            ob2 = other.bend.xVal - mutualPoint.xVal
            if sb2 * ob2 < 0:
                return 0
            if sb > ob:
                
                return ob
            elif sb < ob:
                
                return sb
                
            else:
                
                return sb
        elif mutualPoint.yVal == self.bend.yVal:
            
            
            sb = abs(self.bend.xVal - mutualPoint.xVal)
            ob = abs(other.bend.xVal - mutualPoint.xVal)
            sb2 = self.bend.xVal - mutualPoint.xVal
            ob2 = other.bend.xVal - mutualPoint.xVal
            if sb2 * ob2 < 0:
                return 0

            if sb > ob:
                
                    
                return ob
            elif sb < ob:
                return sb
                
            else:
                
                return sb
        else:
            return 0
    


        
        

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

        #flips the L if there isn't already an overlap, and flips it back if there isn't

        
            
        for value in self.wires:
            connectedwires = self.connectedWires(value)
            value.PrintWire()
            valA = 0
            print(valA)
            for e in connectedwires:
                valA += value.findPotentialOverlap(e)
                print("overlap" + str(valA))
            value.changeBend()
            valB = 0
            print(valB)
            for e in connectedwires:
                valB += value.findPotentialOverlap(e)
                print("overlapb" + str(valB))
            if valA >= valB:
                value.changeBend()
            print("bend:")
            value.bend.PrintPoint()
            print("]]]]]]]]]")

            """
            pick up from here next time 
            """

        for value in self.wires:
            connectedwires = self.connectedWires(value)
            value.PrintWire()
            valA = 0
            for e in connectedwires:
                valA += value.findOverlap(e)
                print("overlap" + str(valA))
            value.changeBend()
            valB = 0
            for e in connectedwires:
                valB += value.findOverlap(e)
                print("overlapb" + str(valB))
            if valA >= valB:
                value.changeBend()
            print("bend:")
            value.bend.PrintPoint()
            print("]]]]]]]]]")
                                    #print(len(connectedwires))
                #for e in connectedwires:
                # e.PrintWire()

    
    #takes the wire passed and returns all the wires connected to it
    def connectedWires(self, wire):
        cwlist = []
        for w in self.wires:
            for e in wire.ends:
                for e2 in w.ends:
                    if e.equals(e2) and not w in cwlist and not wire.wequals(w):
                        cwlist.append(w)
        return cwlist


def convertlist(pts):
    ptlist = []
    for i in pts:
        ptlist.append([i.xVal,i.yVal])
    return ptlist

def wiremaker(ptarr,mstlist,grid):
    for ptpairs in mstlist:
        Wire(Point(ptarr[ptpairs[0]][0],ptarr[ptpairs[0]][1]),Point(ptarr[ptpairs[1]][0],ptarr[ptpairs[1]][1]),grid)
        
def convertwirebendstonodes(grid):
    wirebends = []
    for wire in grid.wires:
        wirebends.append(wire.bend)

#returns a list of wires connected to this wire




#testing
#"""
g = Grid(11,11)
#"""
g.Enable(1,5)
g.Enable(4,4)
g.Enable(2,8)
g.Enable(3,7)
g.Enable(5,9)
g.Enable(7,5)
g.Enable(8,1)
g.Enable(10,2)
g.Enable(10,10)
"""
g.Enable(1,1)
g.Enable(2,4)
g.Enable(4,2)
g.Enable(5,1)
"""
g.PrintGraph()
g.UpdatePoints()
#g.PrintPointList()
print(convertlist(g.points))
print(MST.MST(convertlist(g.points)))

g.PrintWireList()
g.Lsteiner()
g.PrintWireList()
wiremaker(convertlist(g.points),MST.MST(convertlist(g.points)),g)
#g.PrintWireList()
g.Lsteiner()
g.PrintWireList()
#print (parser.parser())
convertwirebendstonodes(g)
#"""






