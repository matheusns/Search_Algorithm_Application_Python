def userInput():
    tmpAdjList = []
    s = []
    e = []

    rows = int (input("insert the number of rows: "))
    columns = int (input("insert the number of columns: "))
    
    adjList = [[0 for x in range(rows)] for y in range(columns)] 
    
    for num in range(rows):
        row = input()
        tmpAdjList.append(row)
    
    for i in range(rows):
        for j in range(columns):
            if tmpAdjList[i][j]=='S':
                s = [i,j]
                adjList[i][j] = 'G'
            elif tmpAdjList[i][j]=='E':
                e = [i,j] 
                adjList[i][j] = 'G'
            else:
                adjList[i][j] = tmpAdjList[i][j]  
    return(adjList,rows,columns,s,e)