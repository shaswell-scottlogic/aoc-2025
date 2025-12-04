def readFile(path):
    file = open(path)
    content = file.read()
    file.close()
    return content

def readFileToLines(path):
    file = open(path)
    content = file.readlines()
    file.close()
    return content

def stripLines(lines):
    return [line.strip() for line in lines]