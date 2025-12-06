def readFile(path):
    file = open(path)
    content = file.read()
    file.close()
    return content

def readFileToLines(path, strip = False):
    file = open(path)
    content = file.readlines()
    file.close()

    if (not strip):
        return content

    return [line.strip() for line in content]

def stripLines(lines):
    return [line.strip() for line in lines]