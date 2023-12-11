input = "input/day10"


# f -> down right
# | -> up down
# - -> left right
# J -> left up
# 7 -> left down
# L -> up right


def getStartPoint(map: list):
    rows = len(map)
    cols = len(map[0])
    for row in range(rows):
        for col in range(cols):
            if map[row][col] == "S":
                return [row, col]


def parseData():
    lines = open(input, "r").read().split("\n")
    map = [[*line] for line in lines if line != ""]
    startPoint = getStartPoint(map)
    return (map, startPoint)

def getStartReplacement(row, col, map):
    top = map[row-1][col]
    right = map[row][col+1]
    bottom = map[row+1][col]
    left = map[row][col-1]

    canGoTop = False
    canGoRight = False
    canGoBottom = False
    canGoLeft = False

    if top == "|" or top == "F" or top == '7':
        # can go top
        canGoTop = True
    if right == "-" or left == "J" or left == "7":
        # can go right
        canGoRight = True
    if bottom == "|" or bottom == "J" or bottom == "L":
        # can go left
        canGoBottom = True
    if left == "-" or left == "F" or left == "L":
        # can go left
        canGoLeft = True
    
    if (canGoTop and canGoRight):
        return "L"
    if (canGoTop and canGoBottom):
        return "|"
    if (canGoTop and canGoLeft):
        return "J"
    if (canGoRight and canGoLeft):
        return "-"
    if (canGoRight and canGoBottom):
        return "F"
    if (canGoBottom and canGoLeft):
        return "7"

def getNextWay(wayFrom, currentStep):
    # print(wayFrom, currentStep)
    if(currentStep == "."):
        raise "you fucked up"

    if wayFrom == None:
        if currentStep == "L": return "right"
        if currentStep == "|": return "up"
        if currentStep == "J": return "left"
        if currentStep == "F": return "right"
        if currentStep == "7": return "down"
        if currentStep == "-": return "right"

    if wayFrom == "down":
        if currentStep == "L": return "right"
        if currentStep == "|": return "down"
        if currentStep == "J": return "left"

    if wayFrom == "up":
        if currentStep == "F": return "right"
        if currentStep == "|": return "up"
        if currentStep == "7": return "left"

    if wayFrom == "left":
        if currentStep == "-": return "left"
        if currentStep == "F": return "down"
        if currentStep == "L": return "up"

    if wayFrom == "right":
        if currentStep == "-": return "right"
        if currentStep == "7": return "down"
        if currentStep == "J": return "up"

def getPathLength(map: list, startPoint: list):
    start = map[startPoint[0]][startPoint[1]]
    currentLocation = [startPoint[0], startPoint[1]]
    length = 0
    wayToNext = getNextWay(None, start)
    while currentLocation != startPoint or length == 0:
        length += 1
        if wayToNext == "down": currentLocation = [
            currentLocation[0] + 1, currentLocation[1]
        ]
        if wayToNext == "up": currentLocation = [
            currentLocation[0] - 1, currentLocation[1]
        ]
        if wayToNext == "left": currentLocation = [
            currentLocation[0], currentLocation[1] - 1
        ]
        if wayToNext == "right": currentLocation = [
            currentLocation[0], currentLocation[1] + 1
        ]
        wayToNext = getNextWay(wayToNext, map[currentLocation[0]][currentLocation[1]])

    return length

def getLoop(map: list, startPoint: list):
    start = map[startPoint[0]][startPoint[1]]
    currentLocation = [startPoint[0], startPoint[1]]
    loop = {(currentLocation[0], currentLocation[1])}
    wayToNext = getNextWay(None, start)
    while currentLocation != startPoint or len(loop) == 1:
        if wayToNext == "down": currentLocation = [
            currentLocation[0] + 1, currentLocation[1]
        ]
        if wayToNext == "up": currentLocation = [
            currentLocation[0] - 1, currentLocation[1]
        ]
        if wayToNext == "left": currentLocation = [
            currentLocation[0], currentLocation[1] - 1
        ]
        if wayToNext == "right": currentLocation = [
            currentLocation[0], currentLocation[1] + 1
        ]
        loop.add((currentLocation[0], currentLocation[1]))
        wayToNext = getNextWay(wayToNext, map[currentLocation[0]][currentLocation[1]])

    return loop

def partOne():    
    map, startPoint = parseData()
    map[startPoint[0]][startPoint[1]] = getStartReplacement(startPoint[0], startPoint[1], map)

    print(getPathLength(map, startPoint) / 2)

def partTwo():    
    map, startPoint = parseData()
    map[startPoint[0]][startPoint[1]] = getStartReplacement(startPoint[0], startPoint[1], map)
    loop = getLoop(map, startPoint)
    map = ["".join(ch if (r, c) in loop else "." for c, ch in enumerate(row)) for r, row in enumerate(map)]

    outside = set()

    for r, row in enumerate(map):
        within = False
        up = None
        for c, ch in enumerate(row):
            if ch == "|":
                assert up is None
                within = not within
            elif ch == "-":
                assert up is not None
            elif ch in "LF":
                assert up is None
                up = ch == "L"
            elif ch in "7J":
                assert up is not None
                if ch != ("J" if up else "7"):
                    within = not within
                up = None
            elif ch == ".":
                pass
            else:
                raise RuntimeError(f"unexpected character (horizontal): {ch}")
            if not within:
                outside.add((r, c))
                
    print(len(map) * len(map[0]) - len(outside | loop))

# 6768
partOne()

# 351
partTwo()