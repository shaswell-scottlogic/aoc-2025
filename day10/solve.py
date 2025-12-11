import utils

def indicatorEntryAsBinary(char):
    return 1 if char=='#' else 0

def indicatorToBinaryString(string):
    return [indicatorEntryAsBinary(char) for char in string]

def buttonAsBinary(buttonString, indicatorLength):
    # each position should be 1 if number exists in buttonNoBrackets, 0 otherwise
    binaryButton = [
        1 if str(i) in buttonString else 0 for i in range(0, indicatorLength)
    ]
    return binaryButton

def indicatorToChangeIndexes(indicator):
    changeIndexes = []
    for index in range(0, len(indicator)):
        if(indicator[index]=='#'):
            changeIndexes.append(index)
    return changeIndexes

def flip(bit):
    return 0 if bit==1 else 1

# expect [1, 0, 0 etc] and (0, 3, 4)
def pressButton(indicator, buttonString):
    # TODO: make this work properly
    for lightNum in buttonString:
        indicator[int(lightNum)] = flip(indicator[int(lightNum)])
    return indicator

# def getPositionsAffected(button):

print("Solve day 10")

lines: list[str] = utils.readFileToLines('./day10/sample', strip = True)

indicator = ''
buttons = []
for line in lines:
    indicator, rest = line.split(']')
    indicator = indicator[1:]
    indicator.strip()
    # bindicator = indicatorToBinaryString(indicator)
    positionsToChange = indicatorToChangeIndexes(indicator)
    # print(bindicator)

    buttonString, rest = rest.split('{')
    buttonString.strip()
    uglyButtonStrings = utils.removeAllInstancesOf(buttonString.split(' '), '')
    buttons = [[int(position) for position in utils.removeAllInstancesOf(singleButton[1: -1].split(','), '')] for singleButton in uglyButtonStrings]
    # print(buttons)

    # TODO: check button arrays are even length-ed

    joltage = rest[:-1]
    joltage.strip()
    # print(joltage)

    # create start string based on length of indicator
    startString = [0 for i in indicator]
    # print(startString)

    # something about hamming distance?
    # can I use hamming distance to select the correct button somehow?
    # is that overkill?
    # do I just need to combine things until done

    # TODO:
    # some combinations of buttons are functionally equivalent to other buttons?
    # some positions are only changed by one button
    # map of position -> buttons that change it?
    # buttons are going to appear in multiple places
    # does that matter? Do buttons need IDs?

    positionButtonMap = {}
    buttonsByChangeCount = {}
    for i in range(0, len(buttons)):
        # print("Button: " + str(button))
        # add button to map at position
        # button = buttons[i]
        for position in buttons[i]:
            # print("Position: " + str(position))
            if(position in positionButtonMap):
                # print("Add button to position list")
                positionButtonMap[position].append(i)
            else:
                # print("Add new list")
                positionButtonMap[position]=[i]

        changeCount = len(buttons[i])
        if(changeCount in buttonsByChangeCount):
            buttonsByChangeCount[changeCount].append(i)
        else:
            buttonsByChangeCount[changeCount] = [i]

    for item in buttonsByChangeCount:
        print(item)

    # for item in positionButtonMap:
    #     print(item)
        # print(positionButtonMap[item])
    
    # if a position needs to change, you have to include a button that changes it
    # sort map keys by number of buttons that affect a position, ascending
    # define a sort key
    def positionMapSortKey(item):
        return len(positionButtonMap[item])
    positionKeys = list(positionButtonMap.keys())
    # print("Unsorted: " + str(positionKeys))
    positionKeys.sort(key=positionMapSortKey)
    # print(positionKeys)

    # TODO: how should I sort lists of buttons within positions? by exactness? asc or desc?
    # length = num positions changed by it

    # TODO: do any of the buttons exactly match positions changed?
    # could translate both to powers of two or something

    # TODO: could also find button combinations that simplify to changing just one position

    # if a button is the only one that changes a position then it's got to be in there at least once
    mandatoryButtons = []
    excludedButtons = []
    for item in positionButtonMap:
        if(item in positionsToChange):
            if(len(positionButtonMap[item])==1):
                mandatoryButtons.append(buttons[positionButtonMap[item][0]])
        else: # position doesn't need to change
            # if there's something in here with length 1, then add it to the excluded list
            for buttonIndex in positionButtonMap[item]:
                if(len(buttons[buttonIndex])==1):
                    excludedButtons.append(buttons[buttonIndex])
    print(mandatoryButtons)
    print(excludedButtons)
    

    # TODO: new starting point is string with the mandatory buttons applied <- check that it's not done already
    for button in mandatoryButtons:
        startString = pressButton(indicator, button)
    
    if(startString == indicator):
        print('Done after mandatory buttons')
    else:
        print('Not done, but maybe closer')
        # now go back to the big list
        # TODO: 

        # and a list of buttons to apply that excludes mandatory and excluded buttons
        # then recurse over combinations of the others

        # recurse looking for combinations of buttons that change the right things
        # ? check for buttons that change the right number of positions first <- FAST
        # use a cache, make the check ignore order (or always sort)

    print()



