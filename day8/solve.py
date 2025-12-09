import utils
import math

def equalCoordinates(a: list[int], b: list[int]):
    # print("checking " + str(a) + " and " + str(b))
    return True if a[0]==b[0] and a[1]==b[1] and a[2]==b[2] else False

def getDistance(a, b):
    return math.sqrt(
        (a[0]-b[0])**2 + 
        (a[1]-b[1])**2 +
        (a[2]-b[2])**2
    )

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
    if a[2] < b[2]:
        return [a, b]
    if a[2] > b[2]:
        return [b, a]
    # should be impossible
    return [a, b]

def coordinateIsInList(coordinate, list):
    if(len(list)==0): return False
    if(any([equalCoordinates(coordinate, item) for item in list])):
        return True
    return False

# circuits are lists of co-ordinates
def getAffectedCircuits(pair: list[list[int]], circuits: list[list[int]]):
    # find all circuits in list that contain either of pair
    affectedCircuits = []
    unaffectedCircuits = []

    for circuit in circuits:
        # print("checking if coordinates are in circuit " + str(pair[0]) + " " + str(pair[1]) + " - " + str(circuit))

        firstInCircuit = coordinateIsInList(pair[0], circuit)
        secondInCircuit = coordinateIsInList(pair[1], circuit)

        # elif should mean each circuit only gets included once
        if(firstInCircuit):
            # print("found coordinate in existing circuit")
            affectedCircuits.append(circuit)
        elif(secondInCircuit):
            # print("found coordinate in existing circuit")
            affectedCircuits.append(circuit)
        else:
            unaffectedCircuits.append(circuit)

    if(len(affectedCircuits) > 2):
        print("More than two circuits affected")
        exit()
    
    # not de-duping these... questionable?
    # print("affected/unaffected: " + str(len(affectedCircuits)) + " / " + str(len(unaffectedCircuits)))
    return [affectedCircuits, unaffectedCircuits]

def mergeCircuits(circuitA, circuitB):
    return circuitA + circuitB

print("Solve day 8")

lines: list[str] = utils.readFileToLines('./day8/input', strip = True)

coordinates = [[int(numberString) for numberString in line.split(",")] for line in lines]
# print(coordinates)

distanceDict = {}

# need to find distance between all points?
# for point at index i, only need to check it against points at i+1 on because the earlier ones will have been done
for i in range(0, len(coordinates)):
    currentBox  = coordinates[i]
    for j in range(i+1, len(coordinates)):
        nextBox = coordinates[j]
        newPair = sortCoordinatePair(currentBox, nextBox)
        # print(newPair)
        # calculate distance and put it in the map
        dist = getDistance(currentBox, nextBox)
        if(dist in distanceDict):
            distanceDict[dist].append([newPair])
        else:
            distanceDict[dist] = [newPair]
    
# print(distanceDict)
# print(distanceDict.keys())
keys = list(distanceDict.keys())
keys.sort()
# print(keys)

pointsAdded = 0
connectionsMade = 0
circuits = []

# iterate over keys
for distance in (keys):
    pairs = distanceDict[distance]
    # print(pairs)
    # iterate over pairs in list
    for pair in pairs:

        # print(pair)
        affectedCircuits, unaffectedCircuits = getAffectedCircuits(pair, circuits)
        # print(" - ")
        # print(affectedCircuits)
        # print(unaffectedCircuits)

        match len(affectedCircuits):
            case 0:
                # adding two new points
                # print("adding points to new circuit")
                affectedCircuits.append([pair[0], pair[1]])
                pointsAdded = pointsAdded + 2
            case 1:
                # only one circuit is affected
                # so it already contains one of the points, and we need to add the other to it
                # print("adding points to existing circuit")
                if pair[0] not in affectedCircuits[0]:
                    affectedCircuits[0].append(pair[0])

                if pair[1] not in affectedCircuits[0]:
                    affectedCircuits[0].append(pair[1])

                pointsAdded = pointsAdded + 1
            case 2:
                # adding no new points, but combining circuits
                # print("merging two circuits")
                affectedCircuits = [ mergeCircuits(affectedCircuits[0], affectedCircuits[1]) ]
                # print(affectedCircuits)

        # replace circuits with a copy with the merges done
        # make a copy without the two indexes
        circuits = affectedCircuits + unaffectedCircuits
        connectionsMade = connectionsMade + 1
        # print(circuits)

    # check if we've hit 1000 points added, NO connections made
    if(connectionsMade >= 1000):
        print(">1000 connections in " + str(len(circuits)) + " circuits")
        break

# print(circuits)
sizes = [len(circuit) for circuit in circuits]
sizes.sort(reverse=True)
print(sizes)
answer = sizes[0]*sizes[1]*sizes[2]
print("Part 1: " + str(answer)) # 79560
