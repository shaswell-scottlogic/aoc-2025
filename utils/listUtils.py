def sumNumbers(numberList: list[int]):
    total = 0
    for number in numberList:
        total = total + int(number) # maybe not necessary but doesn't hurt as long as we're not using floats
    return total

def multiplyNumbers(numberList: list[int]):
    result = 1
    for number in numberList:
        result = result * number
    return result

def removeAllInstancesOf(someList, thingToRemove):
    accumulator = []
    for item in someList:
        if(item != thingToRemove):
            accumulator.append(item)
    return accumulator