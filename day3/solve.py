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
            

print("day 3")

# read input
lines: list[str] = utils.readFileToLines("./day3/input")

# 16907704694511 TOO LOW

lineNumbers = []

# for each line, iterate over finding largest digit that isn't the last one and its index
# then do the same with the substring from that index to the actual end
# turn those two into one number
for line in lines:
    line = line.strip()  

    # to find a number with 12 digits you need to find the highest in first n-11
    # then highest after that up to n-10
    # for everything from 11 down to 0
 
    indexes = []
    startSubstringAt = 0
    endSubstringBefore = len(line)-10
    lastIndexUsed = 0
    for x in range(0, 11):
        substringToSearch = line[startSubstringAt : endSubstringAt]
        # print("finding part " + str(x) + " substring to search: " + substringToSearch)

        lastIndexUsed = startSubstringAt + getIndexOfLargestNumberInString(substringToSearch)
        # print("newIndex is " + str(lastIndexUsed) + "-> " + line[lastIndexUsed])
        indexes.append(lastIndexUsed)

        startSubstringAt = lastIndexUsed + 1
        endSubstringAt = endSubstringAt + 1


    # for n in range(11, -1, -1):
    #     substringStart = lastIndex + 1
    #     # print("substringStart " + str(substringStart))

    #     substring = line[substringStart : -n]
    #     print(substring)

    #     lastIndex = substringStart + getIndexOfLargestNumberInString(substring)
    #     print("newIndex is " + str(lastIndex) + "-> " + line[lastIndex])
    #     indexes.append(lastIndex)

        # print()

    # firstSubstring = line[:-1]
    # indexOfFirstLarge = getIndexOfLargestNumberInString(firstSubstring)

    # startIndexForSecondSubstring = indexOfFirstLarge + 1
    # secondSubstring = line [startIndexForSecondSubstring :]

    # secondLarge = secondSubstring[getIndexOfLargestNumberInString(secondSubstring)]

    # combinedNumber = line[indexOfFirstLarge] + secondLarge
    
    numbersAtIndexes = [line[i] for i in indexes]
    # print("numbers at indexes: " + str(numbersAtIndexes))
    combinedNumber = ''.join(numbersAtIndexes)
    # print(combinedNumber)

    lineNumbers.append(int(combinedNumber))
    # print(lineNumbers)
    # print()
    
print(utils.sumNumbers(lineNumbers))