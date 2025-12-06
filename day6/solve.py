import utils

print("Solve day 6")


# read in input, strip
input: list[str] = utils.readFileToLines("./day6/input", strip=True)

# somehow cut out repeated whitespace in lines?
# -> split lines on space and remove all entries that are empty
lines = [utils.removeAllInstancesOf(line.split(" "), "") for line in input]
# print(problems)

# check that we've got the same number of entries in every line
problemCount = len(lines[0])
if(any([len(line)!=problemCount for line in lines])):
    print("Something is wonky")

# for every index, do the sum
accumulator = 0
for index in range(0, problemCount):
    # TODO: is it always an int?!
    numbers = [int(line[index]) for line in lines[:-1]]
    # print(numbers)

    operator = lines[-1][index]
    # print(operator)

    problemAnswer = 0
    if(operator == "+"):
        problemAnswer = utils.sumNumbers(numbers)
    elif(operator == "*"):
        problemAnswer = utils.multiplyNumbers(numbers)

    accumulator += problemAnswer

# 4277556 / 4951502530386
print("Part 1: sum of problem answers: " + str(accumulator))
