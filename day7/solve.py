import utils

entryLocation = "S"
emptySpace = "."
splitter = "^"
beam="|"

def part1(lines: list[str]):

    # on first line, find the S
    # note where beam will go in next line
    beamInputIndexes = [lines[0].find(entryLocation)]

    splitCount = 0

    for line in lines[1:]:
        newBeamInputIndexes = []

        # print("beam input indexes " + str(len(beamInputIndexes)))
        for i in beamInputIndexes:
            if(line[i]==emptySpace):
                newBeamInputIndexes.append(i)
            elif(line[i]==splitter):
                # print("split!")
                splitCount = splitCount+1
                # if it's a splitter, add the indexes +1 and -1 if they exist
                if(i-1 >= 0):
                    newBeamInputIndexes.append(i-1)
                if(i+1 < len(line)):
                    newBeamInputIndexes.append(i+1)

        # force newBeamInputIndexes to be a set
        beamInputIndexes = set(newBeamInputIndexes)

    print("Part 1: " + str(splitCount))

def part2(lines: list[str]):
    print("Part 2:")

    # on first line, find the S
    # note where beam will go in next line
    beamInputIndexes = [lines[0].find(entryLocation)]
    # cumulativeBeamInputIndexes = []

    # print("lines: " + str(len(lines)))

    splitCount = 0

    # keep an array where each index contains the number of unique paths that lead there
    # e.g. each rejoin gets the sum of its parents

    def replaceWithNumber(thing):
        return 1 if thing=="S" else 0

    # make something that is all zeroes except the S, hopefully
    uniquePathMap = [replaceWithNumber(thing) for thing in lines[0]]

    startHits = 0
    endHits = 0
    for line in lines[1:]:
        continuingBeamInputIndexes = []
        continuingPathMap = [0 for thing in lines]

        # print("beam input indexes " + str(len(beamInputIndexes)))
        for i in beamInputIndexes:
            if(line[i]==emptySpace):
                continuingBeamInputIndexes.append(i)
                continuingPathMap[i] = continuingPathMap[i] + uniquePathMap[i]
            elif(line[i]==splitter):
                # print("split!")
                splitCount = splitCount+1
                # if it's a splitter, add the indexes +1 and -1 if they exist
                if(i-1 >= 0):
                    continuingBeamInputIndexes.append(i-1)
                    continuingPathMap[i-1] = continuingPathMap[i-1] + uniquePathMap[i]
                else:
                    startHits = startHits + 1
                if(i+1 < len(line)):
                    continuingBeamInputIndexes.append(i+1)
                    continuingPathMap[i+1] = continuingPathMap[i+1] + uniquePathMap[i]
                else:
                    endHits = endHits + 1

        uniquePathMap = continuingPathMap
        uniqueContinuingIndexes = set(continuingBeamInputIndexes)

        # _don't_ force to set, just keep all the paths -> WORKS BUT TAKES FOREVER
        # cumulativeBeamInputIndexes = cumulativeBeamInputIndexes + newBeamInputIndexes

        # don't want to do the same work lots of times, so use unique only
        beamInputIndexes = uniqueContinuingIndexes
        # print("now we have " + str(len(beamInputIndexes)))

    # print(uniquePathMap)
    sumUniquePathsToIndex = utils.sumNumbers(uniquePathMap)
    print("sum of unique paths to indexes " + str(sumUniquePathsToIndex))
    print("startHits: " + str(startHits))
    print("endHits " + str(endHits))
    print("paths with starts and ends: " + str(sumUniquePathsToIndex + startHits + endHits))

print("Solve day 7")

lines: list[str] = utils.readFileToLines('./day7/input', strip = True)

# 21 / 1605
part1(lines)

# 40 / 29893386035180
part2(lines)