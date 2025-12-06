def filterToNumeric(string):    
    accumulator = ''
    for char in string:
        if (char.isnumeric()):
            accumulator = accumulator + char
    return accumulator

def filterOutNumeric(string):    
    accumulator = ''
    for char in string:
        if (not char.isnumeric()):
            accumulator = accumulator + char
    return accumulator
