import utils

print("Solve day 6")

# read in input, strip
input: list[str] = utils.readFileToLines("./day6/input")
input = [line.rstrip() for line in input]

# cut out (repeated) whitespace in lines - splitting two spaces on space gives an empty string
splitInputLines = [line.split(" ") for line in input]

operators = utils.removeAllInstancesOf(splitInputLines[-1], "")
problemCount = len(operators)
print("I got " + str(problemCount) + " problems")

def getProblemInputAtIndex_part1(index, lines):
    lines = [utils.removeAllInstancesOf(line, "") for line in lines]
    # print(lines)
    # check that we've got the same number of entries in every line
    if(any([len(line)!=problemCount for line in lines])):
        print("Something is wonky")
        exit()

    return [int(line[index]) for line in lines[:-1]]

def horribleChunking():
    inputLength = max([len(line) for line in input])

    # iterate across input building chunks
    chunks = []
    currentChunk = []
    for i in range(0, inputLength):
        currentCol = [line.ljust(inputLength)[i] for line in input[:-1]]
        # print("Current col is " + str(currentCol))

        if(all([x == ' ' for x in currentCol])):
            # print("found chunk end")
            chunks.append(currentChunk)
            currentChunk = []
        else:
            currentChunk.append(currentCol)

    chunks.append(currentChunk)

    # now each chunk is a problem
    # print(chunks)
    return chunks

# need to chunk the input for part 2
chunks = horribleChunking()
part2Problems = []
for chunk in chunks:
    problem = []
    for rawNumber in chunk:
        number = ''.join(utils.removeAllInstancesOf(rawNumber, " "))

        if(len(number) > 0):
            problem.append(int(number))
    
    part2Problems.append(problem)

# for every index, do the sum
accumulator_part1 = 0
accumulator_part2 = 0
            
# print(problems)
print("I got " + str(len(part2Problems)) + " problems")

for index in range(0, problemCount):
    # TODO: is it always an int?!
    numbers_part1 = getProblemInputAtIndex_part1(index, splitInputLines)
    # print(numbers_part1)

    numbers_part2 = part2Problems[index]

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
# 3263827 / NOT 3253027141130512 - too high -> 8486156119946
print("Part 2: sum of problem answers: " + str(accumulator_part2))
