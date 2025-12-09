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

print("Solve day 9")

lines: list[str] = utils.readFileToLines('./day9/input', strip = True)

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

        # TODO: figure out if it's a useful point pair...?
        # 

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

print(keys)
print(areaDict[keys[0]])
print("Part 1: " + str(keys[0])) # 4749838800
