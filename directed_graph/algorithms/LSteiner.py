import math
from operator import truediv
from time import sleep
from matplotlib.pyplot import connect
#i could just use the chip/node/wire thing but 

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
    
    def MakeMSL(self,rootpt):
        psystem = []
        psystem.append(rootpt)
        temppts = []
        for p in self.points:
            if not p.equals(rootpt):
                temppts.append(p)
        while len(temppts) > 0:
            closest = maxval
            pointone = Point(0,0)
            pointtwo = Point(0,0)
            for pt1 in psystem:
                self.closest(pt1,psystem).PrintPoint()
                    #will change this function to check for the point that best meets the criteria.
                if pt1.GetWireLength(self.closest(pt1,psystem)) < closest:
                    closest = pt1.GetWireLength(self.closest(pt1,psystem))
                    pointone = pt1
                    pointtwo = self.closest(pt1,psystem)
                    #pointtwo.PrintPoint()
                    
            
            Wire(pointone,pointtwo,self)
            print("wire made")
            

            for i in temppts:
                if self.closest(pointone,psystem).equals(i):
                    try:
                        temppts.remove(i)
                        print("got it")
                    except ValueError:
                        print("help me")
            if not pointtwo in psystem:
                psystem.append(pointtwo)
            for ps in psystem:
                #print("points")
                ps.PrintPoint()
                #print("---------")
            #sleep(10)
            #try:
                #temppts.remove(pointtwo)
           # except ValueError:
                #print("NG")
               # pass
            
            #if len(shortpt) > 1:
            
    #returns the closest point based on rectilinear distance
    #if two or more points have the same rectilinear distance, returns the point with the largest difference in y value
    #if two or more points have the same rectilinear distance and difference in y value, returns the point that's further to the right
    def closest(self,point,ommissions):
        leastlen = maxval
        shortestwl = []
        temppts = []
        for o in self.points:
            
            if not o in ommissions and not o in temppts:
                temppts.append(o)
                    
        for p in temppts:
            if point.GetWireLength(p) < leastlen and not point.equals(p):
                leastlen = point.GetWireLength(p)
                shortestwl.clear
                
                shortestwl.append(p)
            elif point.GetWireLength(p) == leastlen and not point.equals(p):
                
                shortestwl.append(p)
        if len(shortestwl) < 1:
            return shortestwl[0]
        else:
            shortesty = []
            leasty = 0
            for p in shortestwl:
                if point.DiffY(p) > leasty and not point.equals(p):
                    leasty = point.DiffY(p)
                    shortesty.clear
                    
                    shortesty.append(p)
                elif point.DiffY(p) == leasty and not point.equals(p):
                    
                    shortesty.append(p)
            if len(shortesty) < 1:
                return shortesty[0]
            else:
                shortestx = []
                leastx = 0
                for p in shortesty:
                    if p.xVal > leastx and not point.equals(p):
                        leastx = p.xVal
                        shortestx.clear
                        
                        shortestx.append(p)
                    elif p.xVal == leastx and not point.equals(p):
                        
                        shortestx.append(p)
                return shortestx[0]
            

    #now for the big stuff
    def Lsteiner(self):

        # space is saved whenever the bend point is inside one of the other wires (between another bend point and 
        # either the start or end point of the first wire)
        # find out which bending saves more space
        # repeat this until no further optimizations are needed
        for value in self.wires:
            connectedwires = []
            for p in value.ends:
                for w in self.wires:
                    for wp in w.ends:
                        if wp.equals(p) and not(w.wequals(value)):
                            connectedwires.append(w)
            for c in connectedwires:
                if not ((value.bend.xVal == c.bend.xVal) and ((value.bend.yVal <= value.start.yVal and value.bend.yVal >= value.end.yVal) or (value.bend.yVal <= value.end.yVal and value.bend.yVal >= value.start.yVal))) or ((value.bend.yVal == c.bend.yVal) and ((value.bend.xVal <= value.start.xVal and value.bend.xVal >= value.end.xVal) or (value.bend.xVal <= value.end.xVal and value.bend.xVal >= value.start.xVal))):
                    value.changeBend()
                    if not ((value.bend.xVal == c.bend.xVal) and ((value.bend.yVal <= value.start.yVal and value.bend.yVal >= value.end.yVal) or (value.bend.yVal <= value.end.yVal and value.bend.yVal >= value.start.yVal))) or ((value.bend.yVal == c.bend.yVal) and ((value.bend.xVal <= value.start.xVal and value.bend.xVal >= value.end.xVal) or (value.bend.xVal <= value.end.xVal and value.bend.xVal >= value.start.xVal))):
                        value.changeBend()


#h
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
g.MakeMSL(Point(1,5))
g.PrintWireList()
g.Lsteiner()
g.PrintWireList()
