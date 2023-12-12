input = "input/day11"

def rotateUniverse(universe: list):
    return ["".join([*line]) for line in zip(*[[*x] for x in universe ][::-1])]


def expandUniverse(universe: list):
    universeClone = universe.copy()
    count = 0
    for idx, row in enumerate(universe):
        if len(set(row)) == 1:
            universeClone.insert(idx + count, row)
            count += 1

    return universeClone

def getExpandIndex(universe: list) -> set:
    rows = []
    for idr, row in enumerate(universe):
        if len(set(row)) == 1:
            rows.append(idr)

    return sorted(rows)

def getStars(universe: list) -> list:
    stars = []
    for rid, row in enumerate(universe):
        for cid, star in enumerate(row):
            if star == "#":
                stars.append((rid, cid))

    return stars

def parseData():
    universe = open(input, "r").read().splitlines()

    return universe

def partOne():
    universe = parseData()
    universe = expandUniverse(universe)
    universe = rotateUniverse(universe)
    universe = expandUniverse(universe)
    stars = getStars(universe)
    count = 0
    starsCount = len(stars)
    for fromStarId in range(starsCount):
        for toStarId in range(fromStarId + 1, starsCount):
            count += abs(stars[fromStarId][0] - stars[toStarId][0])
            count += abs(stars[fromStarId][1] - stars[toStarId][1])
                        
    print(count)
    return count

def partTwo(multiplier = 1000000):
    universe = parseData()
    x = getExpandIndex(universe)
    universe = rotateUniverse(universe)
    y = getExpandIndex(universe)
    universe = rotateUniverse(universe)
    universe = rotateUniverse(universe)
    universe = rotateUniverse(universe)

    stars = getStars(universe)
    multiplier -= 1
    count = 0
    starsCount = len(stars)
    for fromStarId in range(starsCount):
        for toStarId in range(fromStarId + 1, starsCount):
            x1 = stars[fromStarId][0] + (len([i for i in x if i < stars[fromStarId][0]]) * multiplier)
            x2 = stars[toStarId][0] + (len([i for i in x if i < stars[toStarId][0]]) * multiplier)
            count += abs(x2 - x1)
            y1 = stars[fromStarId][1] + (len([i for i in y if i < stars[fromStarId][1]]) * multiplier)
            y2 = stars[toStarId][1] + (len([i for i in y if i < stars[toStarId][1]]) * multiplier)
            count += abs(y2 - y1)
            
    print(count)
    return count
# 10033566
partOne()

# 560822911938
partTwo()
