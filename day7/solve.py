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

print("Solve day 7")

lines: list[str] = utils.readFileToLines('./day7/input', strip = True)

# 21 / 1605
part1(lines)