import utils
import math

# i.e. it's part 1 invalid
def isSameStringTwice(id: str):
    if(len(id)%2 != 0):
        return False
    
    # now split it in two
    halfLength = math.floor(len(id)/2)
    firstHalf = id[:halfLength]
    secondHalf = id[halfLength:]

    if(firstHalf == secondHalf):
        print("That's the same string twice")
        return True
    
    return False

primes = [2, 3, 5, 7, 11]

def containsAnyRepeats(id: str):
    # print(id)
    idLength = len(id)

    # if its length is even then it'd have to be the part1 case 
    # if(idLength%2 == 0):
    #     #print("length is even")
    #     return isSameStringTwice(id)

    if(idLength <= 1):
        return False
    
    # if length is prime, then is it all one number?
    if(idLength in primes):
        # print("length is prime")
        return len(set(id))==1
    
    # print("length is not prime")

    # if length is not prime, then for each prime(?) factor (x less than len/2 where id%x == 0)
    #   is the first substring of that size repeated?
    # how to get prime factors?
    # do I just go through prime numbers up to 11 seeing if they're factors? May well have multiple
    for factor in range(2, 6):

        if(idLength%factor == 0): # this prime is a factor of the length -> worth looking at
            if(factor != idLength):

                # print(str(factor) + " is a factor of length")
                chunkSet = []
                chunkCount = math.floor(idLength/factor)
                for chunkNum in range(0, chunkCount):
                    chunkSet.append(id[(chunkNum*factor) : ((chunkNum+1)*factor)])
                
                # print(set(chunkSet))

                if(len(set(chunkSet)) == 1):
                    # print("That's the same string times " + str(chunkCount))
                    # print()
                    return True

    # print()
    return False

# print("day2")

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
        if( containsAnyRepeats( str(i) ) == True):
           invalidIds.append(i)
    
#print(invalidIds)

# now sum the list
sumInvalid = utils.sumNumbers(invalidIds)

print("Sum of invalid Ids is " + str(sumInvalid))