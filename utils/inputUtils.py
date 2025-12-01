def getNumericInput(prompt, min = None, max = None):
    rawInput = input(prompt)

    if not rawInput.isnumeric():
        print("That wasn't a number")
        return

    number = int(rawInput)

    if (max and number > max) or (min and number < min):
        print("Out of range; min: " + str(min) + " max: " + str(max))
        return

    return number