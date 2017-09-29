import userinput as ui
import heapq
import queue as Q
import heuristic as hrc

# Value considered as Infinite
INF = 100000000000

if __name__ == "__main__":
    
    # User Map Input
    adjList,rows,columns,source,end = ui.userInput()
    # The initial distances should be the greater possible
    currentG = [[INF for x in range(rows)] for y in range(columns)] 
    # The source distance is zero
    currentG[source[0]][source[1]] = 0
    currentNode = source
    # Lists that helps visit the adjacent nodes
    auxX = [0,-1,0,1]
    auxY = [-1,0,1,0]
    # Dictionary that contains all cost along the map 
    costs = {'G': 10, 'A': 150, 'V': 200, 'M': 170, 'C': 170 }
    # List that contais all visited nodes avoiding redundances
    visited = []
    # Nodes' dad dictionary 
    dad = {}
    dad[str(source)] = None
    # Priority Queue
    pq = Q.PriorityQueue()
    pq.put((0,0,currentNode))
    # Cost of assessed nodes
    cont = 0
    # A* Algorithm
    while(not pq.empty()):
        # The top object in the pq
        tmpObj = pq.get()
        # The Node current distance 
        d = tmpObj[1]
        # Current Node
        currentNode = tmpObj[2]
        # print("F = "+str(tmpObj[0])+" G = "+str(d)+" Current Node = "+str(currentNode) )
        if d > currentG[currentNode[0]][currentNode[1]]:
            continue
        if currentNode == end:
            break
        visited.append(currentNode)
        cont+=1
        for i in range(4):
            # The assessed node through currentNode  
            x = currentNode[0]+auxX[i]
            y = currentNode[1]+auxY[i]
            # Conditions to evaluate the current assessed node
            if ( ([x,y] not in visited) and (x>=0 and x<rows) and (y>=0 and y<rows) ):
                # Cost G that considers the currentNode distance to the source + current assessed node cost 
                g = currentG[currentNode[0]][currentNode[1]]+costs[adjList[x][y]]
                # Manhattam distance from the current assessed node to the target node 
                h = hrc.heuristic([x,y],end,50)
                # Total cost to the target node
                f = g+h
                # If pass through the current assessed node generates a smaller g then adds into the pq 
                if g < currentG[x][y]:
                    currentG[x][y] = g
                    pq.put((f,g,[x,y]))
                    # Adds current assessed node's dad                 
                    dad[str([x,y])] = currentNode 
    print()
    print("Cost of assessed nodes = "+str(cont))
    print("Final Cost to achieve "+str(end)+" = "+str(currentG[end[0]][end[1]]))
    coord = end                         
    print("Path traveled:")
    print(coord)
    while(dad[str(coord)]!=None):
        print(dad[str(coord)])
        coord = dad[str(coord)]
