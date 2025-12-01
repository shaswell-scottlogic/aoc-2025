def sumNumbers(numberList: list[int]):
    total = 0
    for number in numberList:
        total = total + int(number) # maybe not necessary but doesn't hurt as long as we're not using floats
    return total