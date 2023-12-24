import sympy

input = "input/day24"


def getLine(point):
    x1,y1,z1, vx, vy, vz = point
    x2 = x1 + vx
    y2 = y1 + vy
    z2 = z1 + vz

    a = (y1 - y2) / (x1 - x2)
    b = y1 - a * x1

    return [(x1,y1,z1), (x2, y2, z2), (vx, vy, vz), (a, b)]

def commonPoint(line1, line2):
    a,b = line1
    c,d = line2

    if a - c == 0:
        return None

    x = (d - b) / (a - c)
    y = (a * x + b)
    return (x, y)

def partOne():
    # min_x = min_y = 7
    # max_x = max_y = 27

    min_x = min_y = 200000000000000
    max_x = max_y = 400000000000000

    hailstones = [list(map(int, hailstone.replace(" @", ",").split((", ")))) for hailstone in open(input).read().splitlines()]
    lines = [getLine(hailstone) for hailstone in hailstones]
    total = 0;
    for i, line1 in enumerate(lines):
        for y, line2 in enumerate(lines[:i]):
            crossing = commonPoint(line1[3], line2[3])
            if crossing == None:
                continue
            x,y = crossing
            if min_x <= x <=max_x and min_y <= y <= max_y:
                if (x - line1[0][0]) * line1[2][0] > 0 \
                    and (y - line1[0][1]) * line1[2][1] > 0 \
                    and (x - line2[0][0]) * line2[2][0] > 0 \
                    and (y - line2[0][1]) * line2[2][1] > 0:                
                    total += 1
    
    print(total)

def partTwo():
    hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in open(input).read().splitlines()]

    xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

    equations = []

    for i, (x, y, z, vx, vy, vz) in enumerate(hailstones):
        equations.append((xr - x) * (vy - vyr) - (yr - y) * (vx - vxr))
        equations.append((yr - y) * (vz - vzr) - (zr - z) * (vy - vyr))
        if i < 2:
            continue
        answers = [soln for soln in sympy.solve(equations) if all(x % 1 == 0 for x in soln.values())]
        if len(answers) == 1:
            break
        
    answer = answers[0]

    print(answer[xr] + answer[yr] + answer[zr])

# 12015
partOne()

# 1016365642179116
partTwo()
