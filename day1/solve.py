import utils
import math

def applyNewInstruction(prev, direction, delta):
    #print("from " + str(prev) + " " + direction + " by " + str(delta))

    newPosition = 0
    if(direction == 'L'):
        newPosition = prev - delta    
    else:
        newPosition = prev + delta

    # print("new " + str(newPosition))
    # print(newPosition%100)
    return newPosition%100

# position here is always a positive number or zero
def getPasses(position, direction, delta):
    numPasses = 0

    # print("position " + str(position))
    # print("direction " + str(direction))
    # print("delta " + str(delta))

    # not a new hit
    if(delta == 0):
        return 0
    
    # number of full rotations
    numPasses = math.floor(delta/100)

    if(position%100 == 0):
        return numPasses

    # partial rotations
    simplifiedDelta = delta%100

    if(direction == 'L'):
        if(simplifiedDelta >= position): # then we're going to or past zero
            return numPasses + 1
    else:
        if(position + simplifiedDelta >= 100): # then we're going to or past zero
            return numPasses + 1
    
    # print("passes " + str(numPasses))
    return numPasses

def part1(lines):
    zeroHits = 0
    position = 50
    zeroPasses = 0

    # for each line, interpret input
    for line in lines:
        print(line)

        # split line by removing first entry
        direction = line[0]
        delta = int(line[1:])

        # do the needful
        newPosition = applyNewInstruction(position, direction, delta)
        if (newPosition == 0):
            zeroHits = zeroHits + 1

        # print("Hits: " + str(zeroHits))

        passes = getPasses(position, direction, delta)
        
        # print("Go " + direction + " by " + str(delta) + " from " + str(position))
        # print("-> passes: " + str(passes))

        zeroPasses = zeroPasses + passes

        position = newPosition
        # print("")

    # (repeat)

    print("Hit zero " + str(zeroHits) + " times") # answer 3 or 1018
    print("Passed zero " + str(zeroPasses) + " times") # answer 6 or 5815

    # print("Combined: " + str(zeroHits + zeroPasses))

print("Solve day 1")

lines: list[str] = utils.readFileToLines('./day1/input')

part1(lines)

