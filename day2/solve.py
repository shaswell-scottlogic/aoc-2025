import utils
import math

def isValidId(id: str):
    if(len(id)%2 != 0):
        return True
    
    # now split it in two
    halfLength = math.floor(len(id)/2)
    firstHalf = id[:halfLength]
    secondHalf = id[halfLength:]
    #print(firstHalf)
    #print(secondHalf)

    if(firstHalf!=secondHalf):
        return True
    
    return False

print("day2")

invalidIds = []

# read line
# split on comma
line = utils.readFile('./day2/input')
ranges = line.split(',')

# for each idRange
for idRange in ranges:
    # get start and end
    [first, last] = idRange.split('-')
    #print(first)
    #print(last)

    firstInt = int(first)
    lastInt = int(last)

    for i in range( firstInt, lastInt+1):
        #print("i is " + str(i))
        if( isValidId( str(i) ) != True):
           invalidIds.append(i)
    
#print(invalidIds)

# now sum the list
sumInvalid = utils.sumNumbers(invalidIds)

print("Sum of invalid Ids is " + str(sumInvalid))