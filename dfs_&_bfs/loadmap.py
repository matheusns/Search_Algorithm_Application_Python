mapInput = []
def loadMap():
    row = []
    for i in range(4):
        row = input("")
        mapInput.append(row)

    for x in range(4):
        for y in range(5):
            # print ("Map["+str(x)+"]"+"["+str(y)+"] = " +str(mapInput[x][y]))
            if(mapInput[x][y]=='3'):
                root = [x,y]
                return root 

def getMap():
    return mapInput