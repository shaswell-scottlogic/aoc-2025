import utils

print("day 4")

lines: list[str] = utils.readFileToLines("./day4/input")
lines = utils.stripLines(lines)

# assuming every line has the same length
lineCount = len(lines)
maxLineIndex = lineCount - 1
colCount = len(lines[0])
maxColIndex = colCount - 1


def getAdjacentCellContents(l, c):
    # line, col co-ordinates
    # (l-1, c-1) (l-1, c) (l-1, c+1)
    # (l, c-1)   (l, c)   (l, c+1)
    # (l+1, c-1) (l+1, c) (l+1, c+1)

    # Doesn't work for tiny grid, only 3x3 +

    # on the top row
    if(l == 0):
        # on the left edge
        if(c == 0):
            return [ lines[l][c+1], lines[l+1][c], lines[l+1][c+1] ]
        # on the right edge
        if(c == maxColIndex):
            return [ lines[l][c-1], lines[l+1][c-1], lines[l+1][c] ]
        # in the middle
        return [ lines[l][c-1], lines[l][c+1], lines[l+1][c-1], lines[l+1][c], lines[l+1][c+1] ]
    
    # on the bottom row
    if(l == maxLineIndex):
        # on the left edge
        if(c == 0):
            return [ lines[l-1][c], lines[l-1][c+1], lines[l][c+1] ]
        # on the right edge
        if(c == maxColIndex):
            return [ lines[l-1][c-1], lines[l-1][c], lines[l][c-1] ]
        # in the middle
        return [ lines[l-1][c-1], lines[l-1][c], lines[l-1][c+1], lines[l][c-1], lines[l][c+1] ]

    # otherwise we're in a middle row
    # on the left edge
    if(c == 0):
        return [ lines[l-1][c], lines[l-1][c+1], lines[l][c+1], lines[l+1][c], lines[l+1][c+1]]
    # on the right edge
    if(c == maxColIndex):
        return [ lines[l-1][c-1], lines[l-1][c], lines[l][c-1], lines[l+1][c-1], lines[l+1][c]]
    # otherwise we're somewhere in the middle and can have everything
    return [ lines[l-1][c-1], lines[l-1][c], lines[l-1][c+1],
            lines[l][c-1], lines[l][c+1],
            lines[l+1][c-1], lines[l+1][c], lines[l+1][c+1],
            ]

def mapCharsInListToOnes(string, charString):
    if(string == charString):
        return 1
    else:
        return 0

# are there @s in 4 of those cells?
def hasAtLeast4AdjacentRolls(line, col):
    # if it's a corner there are only three spots so return false
    if(line == lineCount-1 & col == colCount-1):
        return False
    
    adjacentCells = getAdjacentCellContents(line, col)
    # map @ -> 1, . => 0 then can sum it to get answers
    adjacentCounts = [mapCharsInListToOnes(cell, "@") for cell in adjacentCells]
    
    return utils.sumNumbers(adjacentCounts) >= 4


countAccessible = 0
# need indexes
for l in range(0, lineCount):
    for p in range(0, colCount):
        # position is lines[l][p]
        # print("position is " + lines[l][p])

        # check if there's a roll there
        if(lines[l][p] == "@"):

            if(hasAtLeast4AdjacentRolls(l, p) == False):
                countAccessible = countAccessible +1

# part 1 = 1367
print(str(countAccessible) + " positions are accessible")

# part 2 = 9144
accessibleStore = []
accessibleRollsFound = True
totalAccessibleCount = 0

iterations = 0

while accessibleRollsFound:
    iterations = iterations + 1

    for l in range(0, lineCount):
        for p in range(0, colCount):
            if(lines[l][p] == "@"):
                if(hasAtLeast4AdjacentRolls(l, p) == False):
                    accessibleStore.append([l, p])

    # we didn't find anything else accessible
    if(len(accessibleStore) == 0):
        accessibleRollsFound = False

    # accumulate
    totalAccessibleCount = totalAccessibleCount + len(accessibleStore)

    # now eliminate the ones we're removing
    for [l, p] in accessibleStore:
        lines[l] = lines[l][0:p] + "x" + lines[l][p+1:] # there's got to be a nicer way
    accessibleStore = []

print("Part 2 total accessible: " + str(totalAccessibleCount))
print("Iteration count: " + str(iterations))
