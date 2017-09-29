import queue as Q

pq = Q.PriorityQueue()
pq.put((0,0,[0,1]))
pq.put((0,0,[4,1]))
pq.put((0,0,[4,2]))
pq.put((0,0,[0,2]))

while(not pq.empty()):
    tmpObj = pq.get()
    d = tmpObj[1]
    currentNode = tmpObj[2]
    print("F = "+str(tmpObj[0])+" G = "+str(d)+" Current Node = "+str(currentNode) )