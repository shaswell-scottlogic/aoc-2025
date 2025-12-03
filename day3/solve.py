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

lineNumbers = []

# for each line, iterate over finding largest digit that isn't the last one and its index
# then do the same with the substring from that index to the actual end
# turn those two into one number
for line in lines:
    line = line.strip()   
    firstSubstring = line[:-1]
    # print(firstSubstring)
    indexOfFirstLarge = getIndexOfLargestNumberInString(firstSubstring)
    # print(str(indexOfFirstLarge) + "]: " + line[indexOfFirstLarge])

    startIndexForSecondSubstring = indexOfFirstLarge + 1
    secondSubstring = line [startIndexForSecondSubstring :]
    # print(secondSubstring)

    secondLarge = secondSubstring[getIndexOfLargestNumberInString(secondSubstring)]
    combinedNumber = line[indexOfFirstLarge] + secondLarge
    # print(combinedNumber)

    lineNumbers.append(int(combinedNumber))
    # print(lineNumbers)
    # if(len(lineNumbers) > 2):
    #     lineNumbers.sort()
    #     lineNumbers.reverse()
    #     lineNumbers = lineNumbers[:1]
    # print(lineNumbers)
    # print()
    
print(utils.sumNumbers(lineNumbers))