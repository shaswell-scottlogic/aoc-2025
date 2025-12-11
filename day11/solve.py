import utils

print("Solve day 11")

lines: list[str] = utils.readFileToLines('./day11/input', strip = True)

# directed graph

# read each line, split, load into map
deviceMap = {}
for line in lines:
    label, outs = line.split(':')
    nodes = utils.removeAllInstancesOf(outs.split(" "), "")
    
    if(label in deviceMap):
        deviceMap[label] = deviceMap[label] + nodes
    else:
        deviceMap[label] = nodes

# print(deviceMap)

def followConnections(thisNode, paths):
    if(thisNode == "out"):
        return 1
    connectionsOut = deviceMap[thisNode]
    # print()
    # print(thisNode)
    # print(connectionsOut)
    # follow each one, increment paths when you hit out
    paths = 0
    for newNode in connectionsOut:
        paths = paths + followConnections(newNode, paths)
    
    return paths


# print(followConnections("you", 0)) # 640

def buildPath(thisNode):
    # print("at " + str(thisNode))

    if(thisNode == "out"):
        # print()
        return [[thisNode]]
    
    connectionsOut = deviceMap[thisNode]
    # print("Outs: " + str(connectionsOut))

    newPaths = []
    for newNode in connectionsOut:
        # need to add child paths possible to each parent path        
        childPathExtensions = buildPath(newNode)
        # print(childPathExtensions)
        newPaths = newPaths + [([thisNode] + extension) for extension in childPathExtensions]
        # print(newPaths)
    # print()
    return newPaths

# print(followConnections("svr", 0)) # 8 paths
# thing = buildPath("svr")
print("---------------------------")
# print(thing)#, [])) # 8 paths
# print(len(thing))

# can we construct paths backwards? from dac and fft?
# start at dac, find fft? or vice-versa
# then find paths to dac or to fft
# start at dac, find path to end

nodeCache = {}

def countPathsBetween(currentNode, end, paths):
    if(currentNode in nodeCache):
        return nodeCache[currentNode]

    # print(currentNode)
    if(currentNode == end):
        return 1
    if(currentNode == "out"):
        return 0
    
    connectionsOut = deviceMap[currentNode]
    # follow each one, increment paths when you hit out
    paths = 0
    for newNode in connectionsOut:
        paths = paths + countPathsBetween(newNode, end, paths)
    
    nodeCache[currentNode] = paths
    return paths

startPaths = 0
middlePaths = countPathsBetween('dac', 'fft', 0)
endPaths = 0

if(middlePaths == 0):
    nodeCache = {}
    middlePaths = countPathsBetween('fft', 'dac', 0)
    # print(middlePaths)
    nodeCache = {}
    startPaths = countPathsBetween('svr', 'fft', 0)
    # print(startPaths)
    endPaths = followConnections('dac', 0)
    # print(endPaths)
else:
    # print(middlePaths)
    nodeCache = {}
    startPaths = countPathsBetween('svr', 'dac', 0)
    # print(startPaths)
    endPaths = followConnections('fft', 0)
    # print(endPaths)

print(startPaths * middlePaths * endPaths)

# 15131 is too low -> 367579641755680