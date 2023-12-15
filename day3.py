houseMap = open("day3", "r").read()

visitedUniqueHouses = 1
visitedHouses = []

def walkMap(mapToWalk, location):
    global visitedHouses, visitedUniqueHouses
    visitedHouses.append(location)
    for direction in mapToWalk:
        if direction == "^":
            location = (location[0], location[1] + 1)
        if direction == ">":
            location = (location[0] + 1, location[1])
        if direction == "v":
            location = (location[0], location[1] - 1)
        if direction == "<":
            location = (location[0] - 1, location[1])

        if location in visitedHouses:
            continue
            
        else:
            visitedUniqueHouses += 1
            visitedHouses.append(location)

walkMap(houseMap, (0,0))
print(visitedUniqueHouses)

visitedUniqueHouses = 1
visitedHouses = []
santaMap = houseMap[::2]
roboSantaMap = [*houseMap[1:],houseMap[0]][::2]

walkMap(santaMap, (0,0))
walkMap(roboSantaMap, (0,0))

print(visitedUniqueHouses)