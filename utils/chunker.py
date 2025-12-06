import math

def chunkLine(line: str, chunkSize: int):
    chunks = []
    numChunks = math.ceil(len(line) / chunkSize)
    print("making " + str(numChunks) + " chunks")

    # always allowing for extra
    for i in range(0, numChunks):
        if(len(line) <= chunkSize):
            chunks.append(line)
            break

        thisChunk = line[0 : chunkSize]      
        chunks.append(thisChunk)

        # what if no line left
        line = line[chunkSize :]
    
    if(len(line) != 0): print("Remainder: '" + str(line) + "'")

    return chunks