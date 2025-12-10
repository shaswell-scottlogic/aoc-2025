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

lines: list[str] = utils.readFileToLines('./day9/input', strip = True)

coordinates = [[int(numberString) for numberString in line.split(",")] for line in lines]

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
xShapeRanges = {}
yShapeRanges = {}
# for each sliding window on pair of red tiles, all the ones between are green
for i in range(0, len(coordinates)):
    # last one loops around to first
    currentTile = coordinates[i]
    # print(currentTile)
    prevTile = coordinates[i-1]
    # print(prevTile)

    greenTiles = greenTiles + getPointsBetweenPoints(currentTile, prevTile)

    # figure out which is bigger/smaller, and arrange them as needed
    # if(currentTile[0]==prevTile[0]): # on the same x val
    #     # print("same column")
    #     x = currentTile[0]
    #     newRange = [ prevTile[1], currentTile[1] ]
    #     newRange.sort()
    #     # print("Adding range " + str(newRange) + " to x=" + str(x))
    #     if(x in xShapeRanges):
    #         xShapeRanges[x].append(newRange)
    #     else:
    #         xShapeRanges[x] = [newRange]
    
    # if(currentTile[1]==prevTile[1]): # on the same y val
    #     # print("same row")
    #     y = currentTile[1]
    #     newRange = [ prevTile[0], currentTile[0] ]
    #     newRange.sort()
    #     # print("Adding range " + str(newRange) + "to y=" + str(y))
    #     if(y in yShapeRanges):
    #         yShapeRanges[y].append(newRange)
    #     else:
    #         yShapeRanges[y] = [newRange]

# print(greenTiles)
# print(len(greenTiles))
# print(xShapeRanges)
# print(yShapeRanges)

def getMin(range):
    return range[0]

def mergeRanges(ranges):
    ranges.sort(key = getMin)

    newRanges = []
    currentRange = [0,0]
    for range in ranges:
        range.sort()

        currentMin, currentMax = currentRange
        newMin, newMax = range
        
        # we already know new min >= old min because we sorted it earlier

        # if new min > old max -> new disjoint range
        if(newMin > currentMax):
            if(currentMin != 0):
                newRanges.append(currentRange)
            currentRange = range
        else:
            # if new max is > old max -> extend current range
            if(newMax > currentMax):
                currentRange[1] = newMax
        # if new max is <= old max -> old max covers it

    # one last time to catch the one we were working on
    newRanges.append(currentRange)
    return newRanges

edgeTiles = greenTiles + coordinates + coordinates
# print(str(len(edgeTiles)) + " edge tiles")

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

def sliceToRanges(slice: list[int]):
    # print(slice)
    ranges = []

    currentMin = slice[0]
    currentMax = slice[0]
    i = 1
    while i < len(slice):
        # same number means an incursion OR protrusion
        if(slice[i] == currentMax and currentMin == currentMax):
            if(i==1 or i==len(slice)-1): # repeat at start/end is fine 
                i = i+1
                continue             
            # if i is odd/even
            if(i%2 ==0): # thin incursion - delete both and skip to next
                currentMax = slice[i+1]
            else: # thin protrusion, add silly little range
                ranges.append([currentMin, currentMax])
                currentMin = slice[i+1]
                currentMax = slice[i+1]
                i = i+2
        elif(slice[i] == currentMax+1):# number + 1 means increase max (because we're inclusive)
            currentMax = slice[i]
        elif(currentMin != currentMax): # we're at the end of a range?
                ranges.append([currentMin, currentMax])
                currentMin = slice[i]
                currentMax = slice[i]
        else: # we've found the other side of our range, for now
                currentMax = slice[i]

        i=i+1

    ranges.append([currentMin, currentMax])
    # print(ranges)
    return ranges

xShapeRanges = {}
yShapeRanges = {}
for sliceKey in xSlices:
    xShapeRanges[sliceKey] = sliceToRanges(xSlices[sliceKey])
for sliceKey in ySlices:
    yShapeRanges[sliceKey] = sliceToRanges(ySlices[sliceKey])
# print(xShapeRanges)
# print(yShapeRanges)

for x in xShapeRanges:
    rangeSet = xShapeRanges[x]
    if(len(rangeSet) > 1):
        xShapeRanges[x] = mergeRanges(rangeSet)
for y in yShapeRanges:
    rangeSet = yShapeRanges[y]
    if(len(rangeSet) > 1):
        yShapeRanges[y] = mergeRanges(rangeSet)

# print(xShapeRanges)
# print(yShapeRanges)
print("Merged ranges done")

def pointIsInShape(x, y, edgeTiles, xSlices, ySlices):
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

    # check opposite corners
    c1 = [a[0], b[1]]
    c2 = [a[1], b[0]]

    # if rectangle contains known bad points
    # if range of points in rectangle overlaps with any bad ranges...

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
            # print("Looking at " + str(x) + "," + str(y))
            pointInShape = pointIsInShape(x, y)
            if(not pointInShape ):
                # print("NOPE")
                return False
            
    return True

def isInRange(x: int, range: list[int]):
    min, max = range
    # print("checking if " + str(x) + " is in range " + str(min) + " to " + str(max))

    if(x >= min):
        if(x <= max):
            return True
    return False

def areRectangleEdgesInRanges(rectangle):
    a, b = rectangle
    
    rectangleXRange = [a[0], b[0]] # x range is a horizontal edge, exists at two y vals
    rectangleYRange = [a[1], b[1]] # y range is a vertical edge, exists at two x vals
    # print(rectangleXRange)
    # print(rectangleYRange)

    for y in rectangleYRange: # the two y values where horzontal edges are
        # print("for edge at y=" + str(y))
        # print("Shape Y ranges " + str(yShapeRanges[y]))
        # does x overlap entirely with a range in yRanges[y]
        # carry on if there's any range
        foundAFittingYRange = False
        for yShapeRange in yShapeRanges[y]: # compare shape and rectangles' ranges at y
            # print("checking if " + str(rectangleXRange) + " is in " + str(yShapeRange))
            # if both ends of the edge are within one range then we're good
            if( isInRange(rectangleXRange[0], yShapeRange) and isInRange(rectangleXRange[1], yShapeRange)):
                # we've got a range the edge fits in
                foundAFittingYRange = True
        if(foundAFittingYRange != True):
            # this edge doesn't work
            # print("NOPE")
            return False
        
    # print("Horizontal edges were fine")
    
    for x in rectangleXRange:
        # print("for edge at x=" + str(x))
        # print("Shape X ranges " + str(xShapeRanges[x]))
        # does x overlap entirely with a range in yRanges[y]
        foundAFittingXRange = False
        for xShapeRange in xShapeRanges[x]:
            # print("checking if " + str(rectangleYRange) + " is in " + str(xShapeRange))
            if( isInRange(rectangleYRange[0], xShapeRange) and isInRange(rectangleYRange[1], xShapeRange)):
                # we've got a range the edge fits in
                foundAFittingXRange = True
        if(foundAFittingXRange != True):
            # this edge doesn't work
            # print("NOPE")
            return False        
            
    # print("Vertical edges were fine")
    # print("Rectangle fits in ranges!")
    return True

timeToStop = False
# for candidateRectangle in area dict -> defined by co-ordinates
for key in keys:
    rectangles = areaDict[key]
    # print(rectangles)
    for rectangle in rectangles:
        # print(rectangle)
        rectangle = sortCoordinatePair(rectangle[0], rectangle[1])
        # print("Look at rectangle defined by " + str(rectangle))
        # print("...which has area " + str(key))

        # TODO: doesn't work because ranges are wrong
        if(areRectangleEdgesInRanges(rectangle)):
            print("Part 2: " + str(key)) # 1624057680
            exit()

        # if(areAllPointsInShape(rectangle)):
        #     print("Part 2: " + str(key))
        #     exit()
