input = "input/day18"

# https://en.wikipedia.org/wiki/Shoelace_formula
# https://en.wikipedia.org/wiki/Pick%27s_theorem


def partOne():
    dx = 0
    dy = 0
    x = 0
    y = 0
    path = [(0,0)]
    boundary_points = 0
    instructions = open(input).read().splitlines()
    for instruction in instructions:
        direction, steps, color = instruction.split()
        boundary_points += int(steps)
        if direction == 'R':
            dx = 0
            dy = 1
        if direction == 'D':
            dx = 1
            dy = 0
        if direction == 'U':
            dx = -1
            dy = 0
        if direction == 'L':
            dx = 0
            dy = -1

        x = x + dx * int(steps)
        y = y + dy * int(steps)

        path.append((x, y))

    
    area = 0
    for i in range(len(path) - 1):
        area += path[i][0] * path[i+1][1] - path[i][1] * path[i+1][0]
        
    area = abs(area) // 2
    print(area - boundary_points // 2 + 1 + boundary_points)


def partTwo():
    dx = 0
    dy = 0
    x = 0
    y = 0
    path = [(0,0)]
    boundary_points = 0
    instructions = open(input).read().splitlines()
    for instruction in instructions:
        direction, steps, color = instruction.split()
        steps = int(color[2:-2], base=16)
        direction = color[-2:-1]
        
        boundary_points += int(steps)
        if direction == '0':
            dx = 0
            dy = 1
        if direction == '1':
            dx = 1
            dy = 0
        if direction == '3':
            dx = -1
            dy = 0
        if direction == '2':
            dx = 0
            dy = -1

        x = x + dx * int(steps)
        y = y + dy * int(steps)

        path.append((x, y))

    
    area = 0
    for i in range(len(path) - 1):
        area += path[i][0] * path[i+1][1] - path[i][1] * path[i+1][0]
        
    area = abs(area) // 2
    print(area - boundary_points // 2 + 1 + boundary_points)

# 106459
partOne()
# 63806916814808
partTwo()