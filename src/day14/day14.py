input = "input/day14"

def parseData():
    return open(input, "r").read().splitlines()

def moveRocksLeft(row):
    return "#".join(map("".join, [sorted(list(group), reverse=True) for group in "".join(row).split("#")]))
    # v1 slow :(
    # rocks = [rock for rock in row]
    # while ".O" in "".join(rocks):
    #     for i, rock in enumerate(rocks):
    #         if i == 0 or rock in ".#":
    #             continue
    #         if rocks[i - 1] == '.':
    #             rocks[i], rocks[i - 1] = rocks[i - 1], rocks[i]
        
    # return "".join(rocks)

def moveRocksRight(row):
    row = moveRocksLeft(row[::-1])
    return row[::-1]

def tiltNorth(data: list) -> list:
    rotated = [list(row) for row in list(zip(*data))]
    rotated = [moveRocksLeft(row) for row in rotated]
    data = ["".join(list(row)) for row in list(zip(*rotated))]
    return data

def tiltSouth(data: list) -> list:
    rotated = [list(row) for row in list(zip(*data))]
    rotated = [moveRocksRight(row) for row in rotated]
    data = ["".join(list(row)) for row in list(zip(*rotated))]
    return data

def tiltWest(data: list) -> list:
    return [moveRocksLeft(row) for row in data]

def tiltEast(data: list) -> list:
    return [moveRocksRight(row) for row in data]

def getWeight(data: list) -> list:
    l = len(data)
    count = 0
    for i, c in enumerate(data):
        count+= ((l - i) * sum([ 1 for a in c if a == "O" ]))

    return count

def tiltAllDirector(data):
    for _ in range(4):
        data = [list(row) for row in list(zip(*data))]
        data = [moveRocksLeft(row) for row in data]
        data = [row[::-1] for row in data]
    return data

def partOne():
    data = parseData()
    data = tiltNorth(data)
    print(getWeight(data))

def partTwo():
    data = parseData()
    
    # the same result for 1 000 000 000 and 1 000
    seen = {tuple(data)}
    seenGrids = [data]

    lestSeenGreedId = 0
    while True:
        lestSeenGreedId += 1
        data = tiltAllDirector(data)
        if tuple(data) in seen:
            break

        seen.add(tuple(data))
        seenGrids.append(data)
    
    firstSeenGridId = seenGrids.index(data)
    print(getWeight(seenGrids[(1000000000 - firstSeenGridId) % (lestSeenGreedId - firstSeenGridId) + firstSeenGridId]))
    
# 106517
partOne()

# 79723
partTwo()