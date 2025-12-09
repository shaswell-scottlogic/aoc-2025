import utils
import math

# written badly but probably fine
def sortCoordinatePair(a, b):
    if a[0] < b[0]:
        return [a, b]
    if a[0] > b[0]:
        return [b, a]
    if a[1] < b[1]:
        return [a, b]
    if a[1] > b[1]:
        return [b, a]
    # should be impossible
    return [a, b]

def getDistance(a, b):
    return math.sqrt(
        (a[0]-b[0])**2 + 
        (a[1]-b[1])**2
    )

def getAreaBetweenPoints(a, b):
    # if(a[0]==b[0]):
    #     return abs(a[1]-b[1])#+1
    # if(a[1]==b[1]):
    #     return abs(a[0]-b[0])#+1

    # print("-")
    # print(a)
    # print(b)
    # print(abs(a[0]-b[0])+1)
    # print(abs(a[1]-b[1])+1)
    return (abs((a[0])-(b[0]))+1) * (abs((a[1])-(b[1]))+1)

def getPointsBetweenPoints(a, b):
    points = sortCoordinatePair(a, b)
    # print(" ")
    # print(points)
    # points.reverse()
    a, b = points

    tilesBetween = []
    if(a[0]==b[0]): # on the same column
        # print("same column")
        newEdgeTiles = [ [a[0], a[1] + inc ] for inc in range(1, b[1]-a[1])]
        # print(newEdgeTiles)
        tilesBetween = tilesBetween + newEdgeTiles
    
    if(a[1]==b[1]): # on the same row
        # print("same row")
        newEdgeTiles = [ [a[0] + inc, a[1]] for inc in range(1, b[0]-a[0])]
        # print(newEdgeTiles)
        tilesBetween = tilesBetween + newEdgeTiles
    
    return tilesBetween

print("Solve day 9")

lines: list[str] = utils.readFileToLines('./day9/sample', strip = True)

# find tiles with min and max coordinates in each direction
# find areas in rectangles created by them
# pick the largest

coordinates = [[int(numberString) for numberString in line.split(",")] for line in lines]
# print(coordinates)

areaDict = {}
# for point at index i, only need to check it against points at i+1 on because the earlier ones will have been done
for i in range(0, len(coordinates)):
    currentPoint  = coordinates[i]
    for j in range(i+1, len(coordinates)):
        nextPoint = coordinates[j]

        newPair = sortCoordinatePair(currentPoint, nextPoint)
        # print(newPair)
        # calculate distance and put it in the map
        area = getAreaBetweenPoints(currentPoint, nextPoint)
        if(area in areaDict):
            areaDict[area].append(newPair)
        else:
            areaDict[area] = [newPair]
# print(areaDict)

keys = list(areaDict.keys())
keys.sort(reverse=True)

# print(keys)
# print(areaDict[keys[0]])
print("Part 1: " + str(keys[0])) # 4749838800

# part 2

greenTiles = []
# for each sliding window on pair of red tiles, all the ones between are green
for i in range(0, len(coordinates)):
    # last one loops around to first
    currentTile = coordinates[i]
    # print(currentTile)
    prevTile = coordinates[i-1]
    # print(prevTile)

    greenTiles = greenTiles + getPointsBetweenPoints(currentTile, prevTile)

# print(greenTiles)
# print(len(greenTiles))

edgeTiles = greenTiles + coordinates
print(str(len(edgeTiles)) + " edge tiles")
# TODO: force edge tiles to set?
# TODO: consider sorting?

# TODO: format edge tiles into two listy things?
# e.g. edge at row -> [ 3, 4, 4, 5 ]

xSlices = {}
ySlices = {}
for tile in edgeTiles:
    x, y = tile
    if(x not in xSlices):
        xSlices[x] = [ y ]
    else:
        xSlices[x].append(y)
    xSlices[x].sort()

    if(y not in ySlices):
        ySlices[y] = [ x ]
    else:
        ySlices[y].append(x)
    ySlices[y].sort()


# how do you find what's inside a shape?
# look at all the edge crossings on a line and see if point has crossed an odd or even number of edges?
# ...|...|....
# for thin incursions, double count the edges -> don't dedupe

# for each tile inside the square, is it on an edge?
# how many edges are each side of it in each dimension?

# slice through, by creating an array of edge coordinates sorted by x or y
# for each point you want to check, check the mod value of the last edge coordinate that was less than it

def pointIsInShape(x, y):
    # print(str(x) + "," + str(y))
    if([x,y] in edgeTiles): 
        # print("Is edge, YARP")
        return True

    if(x in ySlices[y] or y in xSlices[x]): # we've hit an edge
        # print("Is edge, YARP - bad")
        return True

    # falls outside the outside edges
    if(x < ySlices[y][0] or x > ySlices[y][-1]):
        # print("Well outside")
        return False
    if(y < xSlices[x][0] or y > xSlices[x][-1]):
        # print("Well outside")
        return False
    
    # otherwise, find last index less than
    for i in range(0, len(ySlices[y])):
        # print(ySlices[y])
        if(ySlices[y][i] > x):
            # print(str(ySlices[y][i]) + " is bigger than " + str(x))
            # print(ySlices[y])
            if(i%2 == 0):
                return False

    for i in range(0, len(xSlices[x])):
        if(xSlices[x][i] > y):
            # print(str(xSlices[x][i]) + " is bigger than " + str(y))
            # print(xSlices[x])
            if(i%2 == 0):
                return False
            
    return True

def areAllPointsInShape(rectangle):
    a, b = rectangle

    xRangeSize = abs(1 + a[0]-b[0])
    if(a[0]>b[0]):
        xStart = b[0]
        xStop = b[0] + xRangeSize
    else:
        xStart = a[0]
        xStop = a[0] + xRangeSize

    # iterate over rectangle, check where in slices points fall
    for x in range(xStart, xStop):
        # print("x" + str(x))
        yRangeSize = abs(1 + a[1]-b[1])
        if(a[1]>b[1]):
            yStart = b[1]
            yStop = b[1] + yRangeSize
        else:
            yStart = a[1]
            yStop = a[1] + yRangeSize
        
        for y in range(yStart, yStop+1):
            # print("y" + str(y))
            print("Looking at " + str(x) + "," + str(y))
            pointInShape = pointIsInShape(x, y)
            if(not pointInShape ):
                # print("NOPE")
                return False
            
    return True


timeToStop = False
# for candidateRectangle in area dict -> defined by co-ordinates
for key in keys:
    rectangles = areaDict[key]
    print(rectangles)
    for rectangle in rectangles:
        print(rectangle)
        rectangle = sortCoordinatePair(rectangle[0], rectangle[1])
        print("Look at rectangle defined by " + str(rectangle))
        if(areAllPointsInShape(rectangle)):
            print("Part 2: " + str(key))
            exit()
        # a, b = rectangle
        # # print(a)
        # # print(b)
        # # iterate over rectangle, check where in slices points fall
        # for x in range(a[0], b[0]+1):
        #     print("x" + str(x))

        #     rangeSize = abs(1 + a[1]-b[1])
        #     if(a[1]>b[1]):
        #         start = b[1]
        #         stop = a[1]
        #     else:
        #         start = a[1]
        #         stop = b[1]
            
        #     for y in range(start, stop):
        #         print("y" + str(y))
        #         print("Looking at " + str(x) + "," + str(y))
        #         if( not pointIsInShape(x, y)):
        #             # how to break out hard enough?
        #             break

# get all the points inside the rectangle
# check if any of them are outside?
# start from the opposite corners


