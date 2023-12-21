from collections import deque

input = "input/day21"

def printGarden(garden_map, locations):
    for i in range(len(garden_map)):
        row = "".join(["O" if (i,j) in locations else garden_map[i][j] for j in range(len(garden_map[i])) ])
        print(row)
    pass

def partOne():
    garden_map = open(input).read().splitlines()
    locations = set()
    for i in range(len(garden_map)):
        if len(locations) > 0:
            break
        for j in range(len(garden_map[0])):
            if garden_map[i][j] == "S":
                locations.add((i, j))
                break

    for i in range(64):
        new_locations = set()
        for location in locations:
            row, col = location
            for delta_row, delta_col in [(0,1),(0,-1),(1,0),(-1,0)]:
                new_row = row + delta_row
                new_col = col + delta_col
                if (new_row >= 0 and new_row < len(garden_map) and new_col >= 0 and new_col < len(garden_map[0])):
                    if (garden_map[new_row][new_col] in '.S'):
                        new_locations.add((new_row, new_col))
        locations = new_locations

    print(len(locations))
    printGarden(garden_map, locations)


def partTwo():
    garden_map = open(input).read().splitlines()
    locations = set()
    for i in range(len(garden_map)):
        if len(locations) > 0:
            break
        for j in range(len(garden_map[0])):
            if garden_map[i][j] == "S":
                locations.add((i, j))
                break
    
    steps = 26501365
    startLocation = locations.pop()
    
    def getLocationsForSteps(start, steps_count):
        locations = set()
        locations.add(start)
        
        for _ in range(steps_count):
            new_locations = set()
            for location in locations:
                row, col = location
                for delta_row, delta_col in [(0,1),(0,-1),(1,0),(-1,0)]:
                    new_row = row + delta_row
                    new_col = col + delta_col
                    if (new_row >= 0 and new_row < len(garden_map) and new_col >= 0 and new_col < len(garden_map[0])):
                        if (garden_map[new_row][new_col] in '.S'):
                            new_locations.add((new_row, new_col))
            locations = new_locations
        
        return len(locations)

    
    full_pages = steps // len(garden_map) - 1
    even = getLocationsForSteps(startLocation, len(garden_map) + 1) * (((full_pages + 1) // 2 * 2) ** 2)
    odd = getLocationsForSteps(startLocation, len(garden_map)) * ((full_pages // 2 * 2 + 1) ** 2)

    remainingSteps = steps % len(garden_map) * 2

    print(sum([
        odd,
        even, 
        getLocationsForSteps((startLocation[0], 0), remainingSteps) +
        getLocationsForSteps((startLocation[0], len(garden_map) - 1), remainingSteps) +
        getLocationsForSteps((0, startLocation[1]), remainingSteps) +
        getLocationsForSteps((len(garden_map) - 1, startLocation[1]), remainingSteps),

        getLocationsForSteps((0,0), len(garden_map) // 2 - 1) * (full_pages + 1)+
        getLocationsForSteps((0,len(garden_map)-1), len(garden_map) // 2 - 1) * (full_pages + 1)+
        getLocationsForSteps((len(garden_map)-1,len(garden_map)-1), len(garden_map) // 2 - 1) * (full_pages + 1)+
        getLocationsForSteps((len(garden_map)-1,0), len(garden_map) // 2 - 1) * (full_pages + 1),

        getLocationsForSteps((0,0), len(garden_map) * 3 // 2 - 1) * full_pages +
        getLocationsForSteps((0,len(garden_map)-1), len(garden_map) * 3 // 2 - 1) * full_pages +
        getLocationsForSteps((len(garden_map)-1,len(garden_map)-1), len(garden_map) * 3 // 2 - 1) * full_pages+
        getLocationsForSteps((len(garden_map)-1,0), len(garden_map) * 3 // 2 - 1) * full_pages
    ]))

    # print(test)


# 42
partOne()

# 606188414811259
partTwo()
