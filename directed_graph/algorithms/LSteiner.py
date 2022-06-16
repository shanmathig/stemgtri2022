import math
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

class Wire:
    start : Point
    end : Point
    bend : Point
    def __init__(self,p1,p2,grid):
        self.start = p1
        self.end = p2
        self.bend = Point(p1.xVal,p2.yVal)
        grid.wires.append(self)

    #changes the bend
    def changeBend(self):
        if self.bend == Point(self.start.xVal,self.end.yVal):
            self.bend = Point(self.end.xVal,self.start.yVal)
        elif self.bend == Point(self.end.xVal,self.start.yVal):
            self.bend = Point(self.start.xVal,self.end.yVal)
    

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

    def makeMSL(self,rootpt):
        mslpts = []
        activept = rootpt
        mslpts.append(activept)

        b = self.makeBranch(activept)
        activept.append(b.end)
        



    #Supplementary functions to help make the msl
    #work in progress

    #makes a wire from a point with some conditions:
    #From the closest three points, the point will connect with the other point...
    #that has the shortest wire length
    #that has the greater difference in Y value
    #that is further to the right
    #this can be simplified a lot probably
    def makeBranch(self,activepoint):
        
        c3 = self.GetClosestThree(activepoint)

        aw = activepoint.GetWireLength(c3[0])
        bw = activepoint.GetWireLength(c3[1])
        cw = activepoint.GetWireLength(c3[2])

        ay = activepoint.DiffY(c3[0])
        by = activepoint.DiffY(c3[1])
        cy = activepoint.DiffY(c3[2])

        ax = c3[0].xVal
        bx = c3[1].xVal
        cx = c3[2].xVal

        closestPoint = c3[0]
        if aw < bw and aw < cw:
            closestPoint = c3[0]
        elif bw < aw and bw < cw:
            closestPoint = c3[1]
        elif cw < aw and cw < bw:
            closestPoint = c3[2]
        elif aw == bw and aw < cw:
            if ay < by:
                closestPoint = c3[0]
            elif by < ay:
                closestPoint = c3[1]
            else:
                if ax < bx:
                    closestPoint = c3[0]
                elif bx < ax:
                    closestPoint = c3[1]
        elif aw == cw and aw < bw:
            if ay < cy:
                closestPoint = c3[0]
            elif cy < ay:
                closestPoint = c3[2]
            else:
                if ax < cx:
                    closestPoint = c3[0]
                elif cx < ax:
                    closestPoint = c3[2]
        elif bw == cw and bw < aw:
            if by < cy:
                closestPoint = c3[1]
            elif cy < by:
                closestPoint = c3[2]
            else:
                if bx < cx:
                    closestPoint = c3[1]
                elif cx < bx:
                    closestPoint = c3[2]
        elif aw == bw and aw == cw:
            if ay < by and ay < cy:
                closestPoint = c3[0]
            elif by < ay and by < cy:
                closestPoint = c3[1]
            elif cy < ay and cy < by:
                closestPoint = c3[2]
            elif ay == by and ay < cy:
                if ax < bx:
                    closestPoint = c3[0]
                elif bx < ax:
                    closestPoint = c3[1]
            elif ay == cy and ay < by:
                if ax < cx:
                    closestPoint = c3[0]
                elif cx < ax:
                    closestPoint = c3[2]
            elif by == cy and by < ay:
                if bx < cx:
                    closestPoint = c3[1]
                elif cx < bx:
                    closestPoint = c3[2]
            elif ay == by and ay == cy:
                if ax < bx and ax < cx:
                    closestPoint = c3[0]
                elif bx < ax and bx < cx:
                    closestPoint = c3[1]
                elif cx < ax and cx < bx:
                    closestPoint = c3[2]
        return Wire(activepoint,closestPoint,self)
    #

    #gets the closest three points that aren't attached to one another
    def GetClosestThree(self,point):
        wl = []
        for p in self.points:
            pinfo = point.GetWireLengthAndPoint(p)
            wl.append(pinfo)
        wl.sort(key=self.GetWL)
        for w in self.wires:
            for index,value in enumerate(wl):
                if (w.start == value['point'] and w.end == point) or (point == w.start and w.end == value['point']):
                    wl.remove(index)
                    index -= 1

        closethree = []
        for i in range(1,4):
            closethree.append(wl[i]['point'])
            #print (wl[i]['point'].PrintPoint())
        return closethree

    #to help with the getclosestthree function
    def GetWL(self,a):
        return a['wirelength']

    #to get the closest point
    #can probably merge the two functions
    def GetClosest(self,point):
        wl = []
        for p in self.points:
            pinfo = point.GetWireLengthAndPoint(p)
            wl.append(pinfo)
        wl.sort(key=self.GetWL)
        for w in self.wires:
            for index,value in enumerate(wl):
                if (w.start == value['point'] and w.end == point) or (point == w.start and w.end == value['point']):
                    wl.remove(index)
                    index -= 1

        closethree = []
        for i in range(1,2):
            closethree.append(wl[i]['point'])
            #print (wl[i]['point'].PrintPoint())
        return closethree


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
g.PrintPointList()
g.makeBranch(Point(1,5))
g.makeBranch(Point(4,4))


