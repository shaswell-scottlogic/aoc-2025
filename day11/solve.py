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

print(deviceMap)

def followConnections(thisNode, paths):
    if(thisNode == "out"):
        return 1
    connectionsOut = deviceMap[thisNode]
    # follow each one, increment paths when you hit out
    paths = 0
    for newNode in connectionsOut:
        paths = paths + followConnections(newNode, paths)
    
    return paths

# recursion while node != out
# for this node, get the nodes this goes to
node = 'you'
getOut = False

print(followConnections("you", 0)) # 640
