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

# position here is always a positive number
def getPasses(position, direction, delta):
    numPasses = 0

    # print("position " + str(position))
    # print("direction " + str(direction))
    # print("delta " + str(delta))

    # if(delta >= 100):
    #     numPasses = math.floor(delta/100)

# add conditions for hitting 100/0

    numPasses = math.floor(delta/100)

    if(direction == 'L'):
        if(delta%100 > position): # then we're going to or past zero
            numPasses = numPasses +1

    else:
        if(position + delta%100 > 100): # then we're going to or past zero
            numPasses = numPasses +1
    
    # print("passes " + str(numPasses))
    return numPasses

def part1(lines):
    zeroHits = 0
    position = 50
    zeroPasses = 0

    # for each line, interpret input
    for line in lines:
        # split line by removing first entry
        direction = line[0]
        delta = int(line[1:len(line)-1])

        # do the needful
        newPosition = applyNewInstruction(position, direction, delta)
        if (newPosition == 0):
            zeroHits = zeroHits + 1

        passes = getPasses(position, direction, delta)
        zeroPasses = zeroPasses + passes

        position = newPosition
        # print("")

    # (repeat)

    print("Hit zero " + str(zeroHits) + " times")
    print("Passed zero " + str(zeroPasses) + " times")

    print("Combined: " + str(zeroHits + zeroPasses))

print("Solve day 1")

lines: list[str] = utils.readFileToLines('./day1/sample')

part1(lines)

