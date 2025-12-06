import utils

print("Solve day 6")

# read in input, strip
input: list[str] = utils.readFileToLines("./day6/sample", strip=True)

# cut out (repeated) whitespace in lines - splitting two spaces on space gives an empty string
inputLines = [line.split(" ") for line in input]
# print(problems)

problemCount = len(utils.removeAllInstancesOf(inputLines[0], ""))
print("I got " + str(problemCount) + " problems")

operators = utils.removeAllInstancesOf(inputLines[-1], "")

def getProblemInputAtIndex_part1(index, lines):
    lines = [utils.removeAllInstancesOf(line, "") for line in lines]
    # print(lines)
    # check that we've got the same number of entries in every line
    if(any([len(line)!=problemCount for line in lines])):
        print("Something is wonky")
        exit()

    return [int(line[index]) for line in lines[:-1]]

def getProblemInputAtIndex_part2(index, lines):
    # actually don't split on space
    # TODO: split each line into chunks of lineLength/problemCount
    # then do this nonsense

    jumblyNumberStrings = [line[index] for line in lines[:-1]]

    # get the length of the longest numberString
    # or iterate, removing
    remainingJumble = jumblyNumberStrings
    piecedNumberStrings = []

    while len(remainingJumble) != 0:
        tempRemaining = []
        newPiecedNumberString =  ""

        for group in remainingJumble:
            print("Looking at group: " + group)
            # take first element and add it
            # newPiecedNumberString += group[0]

            # if there's anything left, keep it for the next round
            # if(len(group) > 1):
            #     tempRemaining.append(group[1:])
        
        piecedNumberStrings.append(newPiecedNumberString)
        remainingJumble = tempRemaining

    return [int(numberString) for numberString in piecedNumberStrings]

# for every index, do the sum
accumulator_part1 = 0
accumulator_part2 = 0

for index in range(0, problemCount):
    # TODO: is it always an int?!
    numbers_part1 = getProblemInputAtIndex_part1(index, inputLines)
    # print(numbers_part1)

    numbers_part2 = getProblemInputAtIndex_part2(index, inputLines)
    print(numbers_part2)

    operator = operators[index]
    # print(operator)

    problemAnswer_part1 = 0
    problemAnswer_part2 = 0
    if(operator == "+"):
        problemAnswer_part1 = utils.sumNumbers(numbers_part1)
        problemAnswer_part2 = utils.sumNumbers(numbers_part2)
    elif(operator == "*"):
        problemAnswer_part1 = utils.multiplyNumbers(numbers_part1)
        problemAnswer_part2 = utils.multiplyNumbers(numbers_part2)

    accumulator_part1 += problemAnswer_part1
    accumulator_part2 += problemAnswer_part2

# 4277556 / 4951502530386
print("Part 1: sum of problem answers: " + str(accumulator_part1))
print("Part 2: sum of problem answers: " + str(accumulator_part2))
