import loadmap as loadMap
import queue

# Stores the map
gridMap = []
# Helper to support look around of the node  
auxX = [0,-1,0]
auxY = [-1,0,1]
# Creates a global list that contais the visited node
visited = []
stop = False
# Total cost
cost = 0
# Creates a dictionary with nodes' dads  
dad = {}
victim_coord = []
path = False

def bfs(robotPose):

    # GLobal variables
    global visited
    global gridMap
    global stop
    global coord
    global auxX
    global auxY
    global cost
    global dad
    global victim_coord

    # Creates a queue
    bfsQueue = queue.Queue(20)
    bfsQueue.put(robotPose)
    dad[str(robotPose)] = None
    stop = False
    victim_coord = []

    while(not bfsQueue.empty() and not stop):
        # Current Node
        currentNode = bfsQueue.get()

        if (currentNode not in visited):
            # print("Current Node = "+str(currentNode))
            visited.append(currentNode)

            for i in range(3):
                x = int(currentNode[0])+auxX[i]
                y = int(currentNode[1])+auxY[i]
                # Current visited node
                coord = [x,y]
                if( coord not in visited and ( (x>=0 and x<=3) and (y>=0 and y<=4) ) ):
                    dad[str(coord)] = currentNode
                    cost+=1
                    # print ("gridMap["+str(x)+"]"+"["+str(y)+"] = " +str(gridMap[x][y]))
                    if(gridMap[x][y] == '1'):
                        bfsQueue.put(coord)
                    elif(gridMap[x][y] == '0'):
                        print("Victim found at the "+str(coord)+" pose!")
                        print("Evaluated nodes total cost = "+str(cost))
                        print()
                        victim_coord = coord            
                        stop = True
    cost = 0
    coord = victim_coord                         
    print("Path traveled:")
    print(coord)
    while(dad[str(coord)]!=None):
        print(dad[str(coord)])
        coord = dad[str(coord)]
        cost+=1
    print("Path cost = "+str(cost))


def dfs(node):

    # Global variables
    global stop
    global coord
    global gridMap
    global visited
    global auxX
    global auxY
    global cost
    global dad
    global victim_coord
    global path
    
    if node not in visited:
        # print("Current Node = "+str(node))
        visited.append(node)
        for i in range(3):
            x = int(node[0])+auxX[i]
            y = int(node[1])+auxY[i]
            coord = [x,y]
            if( (coord not in visited and not stop and (x>=0 and x<=3) and (y>=0 and y<=4) ) ):
                dad[str(coord)] = node 
                if(gridMap[x][y] == '1'):
                    cost+=1
                    # print("Going into: "+str(coord))
                    dfs(coord)
                elif(gridMap[x][y] == '0'):
                    print("Victim found at the "+str(coord)+" pose!")
                    victim_coord = coord
                    print("Total cost = "+str(cost))
                    print()
                    stop = True
        
    if stop and not path:
        coord = victim_coord                         
        print("Path traveled:")
        print(coord)
        cost = 0
        while(dad[str(coord)]!=None):
            print(dad[str(coord)])
            coord = dad[str(coord)]
            cost+=1
        path = True
        print("Path cost = "+str(cost))

if __name__ == '__main__':
    # Loads the Map from user
    chose =int(input("What Technique do you want to use? 1 - BFS || 2 - DSF\n"))
    robotPose = loadMap.loadMap()
    gridMap = (loadMap.getMap())
    # Chose between BFS and DFS
    if(chose==1):
        print("#######")
        print("BFS Chosen")
        print("#######")
        print()
        # Starts the BFS
        bfs(robotPose)
    if(chose==2):
        print("#######")
        print("DFS Chosen")
        print("#######")
        print()
        # Starts the DFS
        global dad
        dad[str(robotPose)] = None
        dfs(robotPose)
