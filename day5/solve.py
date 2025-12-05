import utils
# is there a good way to condense the ranges?
# sort by max then by min? would that give you e.g. (1, 3) (1, 4)?
# then can check if next range is in current range or something

def formatRange(rangeString):
    first, last = rangeString.split('-')

    firstInt = int(first)
    lastInt = int(last)
    return [firstInt, lastInt]

def isInRange(x: int, range: list[int]):
    min, max = range
    # print("checking if " + str(x) + " is in range " + str(min) + " to " + str(max))

    if(x >= min):
        if(x <= max):
            return True
    return False

def rangesOverlap(a, b):
    minA, maxA = a
    minB, maxB = b

    return isInRange(minA, b) | isInRange(maxA, b) | isInRange(minB, a) | isInRange(maxB, a)

def combineRanges(a, b):
    minA, maxA = a
    minB, maxB = b

    minC = minA if minA < minB else minB
    maxC = maxA if maxA > maxB else maxB
    
    return [minC, maxC]

print("Solve day 5")

# read in input, strip
lines: list[str] = utils.readFileToLines("./day5/input")
lines = utils.stripLines(lines)

# split on the whitespace line
emptyLineIndex = lines.index("")
# print("Empty line at index:" + str(emptyLineIndex))

ranges = lines[:emptyLineIndex]
ids = lines[emptyLineIndex+1:]

def getMin(range):
    return range[0]

# turn these things into the format we want
ranges = [formatRange(range) for range in ranges]
ranges.sort(key = getMin)
# [print(range) for range in ranges]

ids = [int(id) for id in ids]
ids.sort()
# [print(id) for id in ids]

# print("Range count: " + str(len(ranges)))
# print("ID count " + str(len(ids)))

# could force to set to dedupe IDs and ranges?
# could condense ranges

candidateIds = ids
freshIds = []

for range in ranges:
    # for candidate Ids
    remainingIds = []

    for id in candidateIds:
        if(isInRange(id, range)):
            freshIds.append(id)
            # print(str(id) + " is fresh because it is in range " + str(range))
        else:
            remainingIds.append(id)

            # if we've gone past the max, skip the rest of the candidate ids
            if(id > range[1]):
                remainingIds = remainingIds + candidateIds[candidateIds.index(id)+1:]
                break
    
    candidateIds = remainingIds
    if(len(remainingIds) == 0):
        break

# print(freshIds)
# 862
print("Part 1: Count of fresh ingredients is: " + str(len(freshIds)))

# part 2 needs to find every ID that is in a range
# can't consider _every_ number, so condense the ranges?

# ASSUME MINS ARE IN ORDER
newRangeSet = []
currentRange = [0,0]
for range in ranges:

        currentMin, currentMax = currentRange
        newMin, newMax = range
        
        # we already know new min >= old min because we sorted it earlier

        # if new min > old max -> new disjoint range
        if(newMin > currentMax):
            if(currentMin != 0):
                newRangeSet.append(currentRange)
            currentRange = range
        else:
            # if new max is > old max -> extend current range
            if(newMax > currentMax):
                currentRange[1] = newMax
        # if new max is <= old max -> old max covers it

# one last time to catch the one we were working on
newRangeSet.append(currentRange)

# now we have all the ranges, count how many IDs they cover
idCount = 0
for range in newRangeSet:
    idCount += (range[1]-range[0]) +1

# 357907198933892
print("Part 2 id count: " + str(idCount))
