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
            areaDict[area].append([newPair])
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
print(len(edgeTiles))
# TODO: force edge tiles to set?
# TODO: consider sorting?

# find all edge tiles = green and red

# how do you find what's inside a shape?
# look at all the edge crossings on a line and see if point has crossed an odd or even number of edges?
# ...|...|....

# for each tile inside the square, is it on an edge?
# how many edges are each side of it in each dimension?


