import utils

def getIndexOfLargestNumberInString(string):
    largest = 0
    indexOfLargest = 0

    # print("finding largest number in " + string)
    # print("length of string is " + str(len(string)))

    if(len(string) == 1):
        return 0

    for i in range(len(string)):
        # print("i: " + str(i))
        charAsInt = int(string[i])
        # print("string[i]: " + string[i])

        if(charAsInt > largest):
            largest = charAsInt
            indexOfLargest = i
            # print("new largest: " + string[i] + " at position " + str(i))
    
    return indexOfLargest

# for each line, iterate over finding largest digit that isn't the last one and its index
# then do the same with the substring from that index to the actual end
# turn those two into one number
def getLargestTwoDigitNumber(line):
    firstSubstring = line[:-1]
    indexOfFirstLarge = getIndexOfLargestNumberInString(firstSubstring)

    startIndexForSecondSubstring = indexOfFirstLarge + 1
    secondSubstring = line [startIndexForSecondSubstring :]

    secondLarge = secondSubstring[getIndexOfLargestNumberInString(secondSubstring)]

    combinedNumber = line[indexOfFirstLarge] + secondLarge
    return combinedNumber

def getLargestTwelveDigitNumber(line):
    indexes = []
    startSubstringAt = 0
    endSubstringBefore = len(line)-11
    lastIndexUsed = 0
    for x in range(0, 12):
        # print()
        # print("x: " + str(x))
        # print("startSubstringAt: " + str(startSubstringAt))
        # print("endSubstringBefore: " + str(endSubstringBefore))
        # print("lastIndexUsed is " + str(lastIndexUsed))

        substringToSearch = line[startSubstringAt : endSubstringBefore]
        # print("finding part " + str(x) + " substring to search: " + substringToSearch)

        lastIndexUsed = startSubstringAt + getIndexOfLargestNumberInString(substringToSearch)
        indexes.append(lastIndexUsed)

        startSubstringAt = lastIndexUsed + 1
        endSubstringBefore = endSubstringBefore + 1
        if(endSubstringBefore >= len(line)):
            endSubstringBefore = len(line)


    numbersAtIndexes = [line[i] for i in indexes]
    # print("numbers at indexes: " + str(numbersAtIndexes))
    combinedNumber = ''.join(numbersAtIndexes)
    return int(combinedNumber)

#####################################################################
print("day 3")

# read input
lines: list[str] = utils.readFileToLines("./day3/input")

# part 1 answer?
# 17034

# part 2 answers:
# 16907704694511 TOO LOW
# 168798209663590 YES

part1Numbers = []
part2Numbers = []

for line in lines:
    line = line.strip()  
    
    part1Numbers.append(getLargestTwoDigitNumber(line))
    part2Numbers.append(getLargestTwelveDigitNumber(line))
    
print("Part 1 answer is " + str(utils.sumNumbers(part1Numbers)))
print("Part 2 answer is " + str(utils.sumNumbers(part2Numbers)))