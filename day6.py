input = "day6"

instructions = open(input, 'r').read().splitlines()

gridPartOne = [[-1 for _ in range(1000)] for _ in range(1000)]
gridPartTwo = [[-1 for _ in range(1000)] for _ in range(1000)]

def partOne():
    global gridPartOne
    for instruction in instructions:
        action, *rest = instruction.split(" ")

        if action == 'turn':
            state = 1 if rest[0] == 'on' else -1
            fromLoc = list(map(int, rest[1].split(",")))
            toLoc = list(map(int, rest[3].split(",")))

            for rowId in range(fromLoc[0], toLoc[0]+1):
                for colId in range(fromLoc[1], toLoc[1]+1):
                    gridPartOne[rowId][colId] = state

        if action == 'toggle':
            fromLoc = list(map(int, rest[0].split(",")))
            toLoc = list(map(int, rest[2].split(",")))

            for rowId in range(fromLoc[0], toLoc[0]+1):
                for colId in range(fromLoc[1], toLoc[1]+1):
                    gridPartOne[rowId][colId] *= -1

    total = 0
    for row in gridPartOne:
        for col in row:
            if col == 1:
                total += 1
    print(total)


gridPartTwo = [[0 for _ in range(1000)] for _ in range(1000)]


def partTwo():
    for instruction in instructions:
        action, *rest = instruction.split(" ")
        if action == 'turn':
            fromLoc = list(map(int, rest[1].split(",")))
            toLoc = list(map(int, rest[3].split(",")))

            for rowId in range(fromLoc[0], toLoc[0]+1):
                for colId in range(fromLoc[1], toLoc[1]+1):
                    if rest[0] == 'on':
                        gridPartTwo[rowId][colId] += 1
                    if rest[0] == 'off' and gridPartTwo[rowId][colId] > 0:
                        gridPartTwo[rowId][colId] -= 1

        if action == 'toggle':
            fromLoc = list(map(int, rest[0].split(",")))
            toLoc = list(map(int, rest[2].split(",")))

            for rowId in range(fromLoc[0], toLoc[0]+1):
                for colId in range(fromLoc[1], toLoc[1]+1):
                    gridPartTwo[rowId][colId] += 2
                    

    total = sum([sum(row) for row in gridPartTwo])
    print(total)
        

# 569999
partOne()
# 17836115
partTwo()