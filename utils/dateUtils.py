import datetime
import utils

def getDayToUse():
    day = utils.getNumericInput("What day should I run? ", 1, 31)

    if day:
        return day

    print('Input unusable, using current date instead')
    return getDayOfMonth()

def getDayOfMonth():
    return datetime.datetime.now().day