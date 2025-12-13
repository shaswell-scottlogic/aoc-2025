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

# expect [1, 0, 0 etc] and button [1, 3, 5]
def pressButton(oldIndicator, button):
    newIndicator = []
    for i in range (0, len(oldIndicator)):
        if(i in button):
            newIndicator.append(flip(oldIndicator[i]))
        else:
            newIndicator.append(oldIndicator[i])
    return newIndicator

# def getPositionsAffected(button):

print("Solve day 10")

lines: list[str] = utils.readFileToLines('./day10/sample', strip = True)

indicator = ''
buttons = []
for line in lines:
    indicator, rest = line.split(']')
    indicator = indicator[1:]
    indicator.strip()
    bindicator = indicatorToBinaryString(indicator)
    positionsToChange = indicatorToChangeIndexes(indicator)
    # print(bindicator)

    buttonString, rest = rest.split('{')
    buttonString.strip()
    uglyButtonStrings = utils.removeAllInstancesOf(buttonString.split(' '), '')
    buttons = [[int(position) for position in utils.removeAllInstancesOf(singleButton[1: -1].split(','), '')] for singleButton in uglyButtonStrings]
    # print(buttons)
    # BUTTONS ARE NOW LIST[INT]

    # TODO: check button arrays are even length-ed

    joltage = rest[:-1]
    joltage.strip()
    # print(joltage)

    # create start string based on length of indicator
    startString = [0 for i in indicator]
    # print(startString)

    # something about hamming distance?
    # can I use hamming distance to select the correct button somehow?
    # is that overkill? do I just need to combine things until done

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

    # for item in buttonsByChangeCount:
        # print(item)

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
                mandatoryButtons.append(positionButtonMap[item][0])
        else: # position doesn't need to change
            # if there's something in here with length 1, then add it to the excluded list
            for buttonIndex in positionButtonMap[item]:
                if(len(buttons[buttonIndex])==1):
                    excludedButtons.append(buttonIndex)
    print(mandatoryButtons)
    print(excludedButtons)
    print()
    
    # Off we go
    workingString = startString
    print("Aiming for " + str(bindicator))

    # so apply the mandatory buttons
    for buttonIndex in mandatoryButtons:
        workingString = pressButton(workingString, buttons[buttonIndex])
        print(workingString)
    
    if(len(mandatoryButtons) >= 1):
        if(workingString == bindicator):
            print('Done after mandatory buttons')
        else:
            print('Not done, but maybe closer')


    # now we find which buttons we have left to explore
    nope = mandatoryButtons + excludedButtons
    # print("nope " + str(nope))
    remainingButtonIndexes = [x for x in list(range(0, len(buttons))) if x not in nope]

    # now we've reduced the problem size
    # print("starting with " + str(workingString))
    # print("remaining button indexes: " + str(remainingButtonIndexes))
    # print(buttons)

    # recurse over combinations of the others
    # with a cache so that we don't repeat sub-groups? Or just pass remaining[1:]
    # def checkNextButton(state, thisButtonIndex, remainingButtonIndexes):        
    #     newState = pressButton(state, buttons[thisButtonIndex])

    #     if(newState == bindicator): # we're done
    #         print("Boom " + str(thisButtonIndex))
    #         return [[thisButtonIndex]] # only if after applying
        
    #     if(len(remainingButtonIndexes) == 0): # hit a dead end
    #         print("Run out of buttons")
    #         return []
    #     # if(newState == startString): # is getting back to an earlier state bad? won't happen if there were any mandatory buttons

    #     newButtonCombinations = []
    #     buttonsMinusThisOne = [x for x in remainingButtonIndexes if x != thisButtonIndex]
    #     # print("buttonsMinusThisOne " + str(buttonsMinusThisOne))
    #     # for each button, call this on other set
    #     for buttonIndex in buttonsMinusThisOne:
    #         childButtonCombinations = checkNextButton(newState, buttonIndex, buttonsMinusThisOne)
    #         if(len(childButtonCombinations)!=0):
    #             # print("cool, add that")
    #             print("Got: " + str(childButtonCombinations))
    #             print("Need to add it to " + str(newButtonCombinations))
    #             newButtonCombinations = newButtonCombinations + [([thisButtonIndex] + c) for c in childButtonCombinations]
    #             print("combinations: " + str(newButtonCombinations))

    #     return newButtonCombinations

        # recurse looking for combinations of buttons that change the right things
        # ? check for buttons that change the right number of positions first <- FAST
        # use a cache, make the check ignore order (or always sort)

    buttonComboCache = []
    def checkButtons(existingState, remainingBIndexes):
        print("New iteration ---------------")

        # what does this do? does it keep the path?
        if( len(remainingBIndexes) == 0 ):
            print("Run out of buttons")
            return []

        remainingBIndexes.sort()
        if(remainingBIndexes in buttonComboCache):
            print("cache hit")
            return []
        else:
            print("cache miss")
            buttonComboCache.append(remainingBIndexes)

        newButtonCombinations = []
        for buttonIndex in remainingBIndexes:
            print("buttonIndex is: " + str(buttonIndex))
            print("Button is " + str(buttons[buttonIndex]))
            newState = pressButton(existingState, buttons[buttonIndex])
            childButtonCombinations = []

            if(newState == bindicator): # we're done
                print("Boom " + str(buttonIndex))
                childButtonCombinations = [[buttonIndex]]
            else:
                print("Looking at a child")
                buttonsMinusThisOne = [x for x in remainingBIndexes if x != buttonIndex]
                print("Buttons minus this one: " + str(buttonsMinusThisOne))
                childButtonCombinations = checkButtons(newState, buttonsMinusThisOne)

            if( len(childButtonCombinations) != 0):
                print()
                print("Got child combos: " + str(childButtonCombinations))
                extendedChildButtonCombos = [(c + [buttonIndex]) for c in childButtonCombinations]
                print("With this node added: " + str(extendedChildButtonCombos))
                newButtonCombinations = newButtonCombinations + extendedChildButtonCombos
                print("Accumulated: " + str(newButtonCombinations))
                print()
        
        # pathsWithThisNode = [(c + [buttonIndex]) for c in newButtonCombinations]
        print("After this iteration: " + str(newButtonCombinations))
        return newButtonCombinations

    # TODO: need to refactor to not need to apply button straight away? Otherwise we start assuming too many buttons
    # answers = checkNextButton(workingString, remainingButtonIndexes[0], remainingButtonIndexes)
    answers = checkButtons(workingString, remainingButtonIndexes)
    for combo in answers:
        print("Combo:")
        print("buttons at indexes " + str(combo))# + mandatoryButtons))
        print("mandatory: " + str(mandatoryButtons))

        print("buttons: " + str([buttons[i] for i in combo + mandatoryButtons]))
        # print(mandatoryButtons)

    exit() # do one only
    print()



