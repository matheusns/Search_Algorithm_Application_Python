def heuristic(source,end,D=50):
    
    deltaX = abs(end[0]-source[0])
    deltaY = abs(end[1]-source[1])

    return D*deltaY*deltaX
