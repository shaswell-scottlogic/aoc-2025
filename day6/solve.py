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

def getNumbersFromChunkColumn(column):
    # works because I chunked with pad=True
    chunkSize = len(column[0])

    # we're getting chunksize=4 numbers
    numbers = []
    for i in range (0, chunkSize):
        newNumberString = [chunk[i] for chunk in column]
        # print(newNumberString)
        newNumberString = utils.removeAllInstancesOf(newNumberString, " ")
        newNumber = ''.join(newNumberString)

        if(len(newNumber)>0):
            numbers.append(int(newNumber))
    return numbers

# for every index, do the sum
accumulator_part1 = 0
accumulator_part2 = 0

# need to chunk the input here for part 2
# chunks are the numbers as strings with the whitespace in
chunks = [utils.chunkLineInto(line, problemCount, pad=True) for line in input[:-1]]
# print(chunks)

for index in range(0, problemCount):
    # TODO: is it always an int?!
    numbers_part1 = getProblemInputAtIndex_part1(index, splitInputLines)
    # print(numbers_part1)

    column = [chunk[index] for chunk in chunks]
    # print(column)
    numbers_part2 = getNumbersFromChunkColumn(column)

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
# 3263827 / NOT 3253027141130512 - too high
print("Part 2: sum of problem answers: " + str(accumulator_part2))
