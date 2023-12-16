input = "input/day16"

grid = open(input).read().splitlines()

def move(beam):
    global grid
    xVelocity = beam["velocity"][0]
    yVelocity = beam["velocity"][1]
    currentLocation = beam["location"]
    newXLocation = currentLocation[0] + xVelocity
    newYLocation = currentLocation[1] + yVelocity
    if newXLocation < 0 or newXLocation >= len(grid) or newYLocation < 0 or newYLocation >= len(grid[0]):
        # beam out of grid
        return []
    
    if grid[newYLocation][newXLocation] == ".":
        return [{ "velocity": (xVelocity, yVelocity), "location": (newXLocation, newYLocation) }]
    if grid[newYLocation][newXLocation] == "/":
        # [1,0] -> [0,-1]
        # [-1,0] -> [0,1]
        # [0,1] -> [-1,0]
        # [0,-1] -> [1,0]
        return [{ "velocity": (yVelocity * -1 , xVelocity * - 1), "location": (newXLocation, newYLocation) }]

    if grid[newYLocation][newXLocation] == "\\":
        # [1,0] -> [0,1]
        # [-1,0] -> [0,-1]
        # [0,1] -> [1,0]
        # [0,-1] -> [-1,0]
        return [{ "velocity": (yVelocity , xVelocity), "location": (newXLocation, newYLocation) }]

    if grid[newYLocation][newXLocation] == "|":
        # [1,0] -> [0,1],[0,-1]
        # [-1,0] -> [0,-1],[0,1]
        # [0,1] -> [1,0]
        # [0,-1] -> [0,-1]
        if xVelocity:
            return [
                { "velocity": (yVelocity , xVelocity), "location": (newXLocation, newYLocation) },
                { "velocity": (yVelocity * -1 , xVelocity * -1), "location": (newXLocation, newYLocation) }
                ]

        return [{ "velocity": (xVelocity, yVelocity), "location": (newXLocation, newYLocation) }]

    if grid[newYLocation][newXLocation] == "-":
        if yVelocity:
            return [
                { "velocity": (yVelocity , xVelocity), "location": (newXLocation, newYLocation) },
                { "velocity": (yVelocity * -1 , xVelocity * -1), "location": (newXLocation, newYLocation) }
                ]

        return [{ "velocity": (xVelocity, yVelocity), "location": (newXLocation, newYLocation) }]

    return beam

def getEnergizedTiles(startingBeam) -> int:
    beams = [startingBeam]
    seen = set()
    locations = set()
    path = []
    while (len(beams)):
        newBeams = []
        for beam in beams:
            newBeam = (beam["velocity"], beam["location"]) 
            if newBeam in seen:
                continue
            if beam["location"] != startingBeam["location"]:
                locations.add(beam["location"])
                path.append(beam["location"])
                seen.add(newBeam)
            next = move(beam)
            for b in next:
                newBeams.append(b)
        
        beams = newBeams
    
    return len(locations)

def partOne():
    global grid
    energizedTilesCount = getEnergizedTiles({ "velocity": (1, 0), "location": (-1, 0) })
    print(energizedTilesCount)

def isLocationInsideTheGrid(location):
    global grid
    if location[0] < 0 or location[0] >= len(grid[0]):
        return False

    if location[1] < 0 or location[1] >= len(grid):
        return False
    
    return True

def partTwo():
    global grid
    velocityRight = (1, 0)
    velocityLeft = (-1, 0)
    velocityBottom = (0, 1)
    velocityTop = (0, -1)

    largestEnergizedTiles = 0

    for rowId in range(len(grid)):
        energizedTilesCount = getEnergizedTiles({"velocity": velocityRight, "location": (-1, rowId)})
        if largestEnergizedTiles < energizedTilesCount:
            largestEnergizedTiles = energizedTilesCount
        energizedTilesCount = getEnergizedTiles({"velocity": velocityLeft, "location": (len(grid[0]), rowId)})
        if largestEnergizedTiles < energizedTilesCount:
            largestEnergizedTiles = energizedTilesCount


    for colId in range(len(grid[0])):
        energizedTilesCount = getEnergizedTiles({"velocity": velocityBottom, "location": (colId, -1)})
        if largestEnergizedTiles < energizedTilesCount:
            largestEnergizedTiles = energizedTilesCount
        
        energizedTilesCount = getEnergizedTiles({"velocity": velocityTop, "location": (colId, len(grid))})
        if largestEnergizedTiles < energizedTilesCount:
            largestEnergizedTiles = energizedTilesCount
    
    print(largestEnergizedTiles)

# 6795
partOne()
        
# 7154
partTwo()