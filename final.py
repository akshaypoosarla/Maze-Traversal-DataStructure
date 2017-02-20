import sys,random
cell=[]
class MazeCell:
    
    #CellWalls=["1111"]
   
    Visited=False
   
    def __init__(self,bool):
        self.Visited = bool
    
    #def PrintWalls(index):
        #print(MazeCell.CellWalls)
   
    #def PickNeighbor(Neighbors):
        #print("Picked a Neighbor")
        #return


def GenerateMaze(cell,h,w):
    height=h+5
    width=w+5
    
   
    Maze=[MazeCell]*width
    for i in range(width):
        Maze[i]=[MazeCell]*height
    
  
    CellStack=[]
   
    CellsTotal = width*height
   
    CellsConsumed=0
    
    print("set current cell")
    CellCurrent=cell
    Maze[CellCurrent[0]][CellCurrent[1]].Visited=True
    CellStack.append(CellCurrent)
    
    North=[0,1]
    East=[1,0]
    South=[0,-1]
    West=[-1,0]
    

   
    for i in range(0,(h)):
        for j in range(0,w):
            Maze[i][j]= MazeCell(False)
            print("MazeCell created at coordinates: "+str(i)+","+str(j))
    
    
    def TestCell(direction):
      
        
        x=direction[0]+CellCurrent[0]
        y=direction[1]+CellCurrent[1]
       
        if x<0 or y<0:
            
            return 0
        elif x>width or y>height:
            
            return 0
        
        
        elif Maze[x][y].Visited==True: 
            return 0
       
        else: return direction
    
    
    def GetNeighbors(Cell):
       
        Neighbors=[]
        
        CNorth=TestCell(North)
        CEast=TestCell(East)
        CSouth=TestCell(South)
        CWest=TestCell(West)
        if CNorth:
            Neighbors.append(CNorth)
        if CEast:
            Neighbors.append(CEast)
        if CSouth:
            Neighbors.append(CSouth)
        if CWest:
            Neighbors.append(CWest)
        print("Nei:",Neighbors)
        return Neighbors
   

    while CellsConsumed < CellsTotal and len(CellStack)>0:
        
        CellNeighbors = GetNeighbors(CellCurrent)
        if len(CellNeighbors)>0:
           
            NeighborChoice=CellNeighbors[random.randrange(0,len(CellNeighbors))]
            print("Direction: "+str(NeighborChoice))
            CellNeighbor=[CellCurrent[0]+NeighborChoice[0],CellCurrent[1]+NeighborChoice[1]]
            print("Chosen Cell: "+str(CellNeighbor))
            CellStack.insert(0,CellNeighbor )
            Maze[CellNeighbor[0]][CellNeighbor[1]].Visited=True
            CellsConsumed += 1
        else:
            print("No Neighbors Found: Pop Stack")
            CellStack.pop()
            i=1           
            while i<len(CellStack):
                CellCurrent=CellStack.pop()
                print ("CurrentCell:",CellCurrent)
                i=i+1
        print("Cell Stack: "+str(CellStack))   
            
            
    return

print ("#########################MAZE########################")
a=int(input("Width"))
b=int(input("Height"))
print ("Enter the current cell:")
q=int(input("1st:"))
cell.append(q)
w=int(input("2nd:"))
cell.append(w)

GenerateMaze(cell,a,b)
