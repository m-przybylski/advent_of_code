input = "day18"

grid = open(input).read().splitlines()
grid = list(map(list, grid))

# on and 2,3 neighbors are on -> on, else off
# off and 3 neighbors are on -> on

step_count = 100

def step(grid):
    new_grid = [row[:] for row in grid]
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            # on state
            if col == "#":
                count = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        if -1 < i + di < len(grid) and -1 < j + dj < len(row) and grid[i + di][j + dj] == "#":
                            count += 1
                if count not in [2, 3]:
                    new_grid[i][j] = '.'
            if col == ".":
                count = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        if -1 < (i + di) < len(grid) and -1 < (j + dj) < len(row) and grid[i + di][j + dj] == "#":
                            count += 1
                if count == 3:
                    new_grid[i][j] = '#'

    return new_grid

def step_corner(grid):
    new_grid = [row[:] for row in grid]
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if (i == 0 and j == 0) or (i == 0 and j == len(row) - 1) or (i == len(grid) - 1 and j == 0) or (i == len(grid) - 1 and j == len(row) - 1):
                continue
            # on state
            if col == "#":
                count = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        if -1 < i + di < len(grid) and -1 < j + dj < len(row) and grid[i + di][j + dj] == "#":
                            count += 1
                if count not in [2, 3]:
                    new_grid[i][j] = '.'
            if col == ".":
                count = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        if -1 < (i + di) < len(grid) and -1 < (j + dj) < len(row) and grid[i + di][j + dj] == "#":
                            count += 1
                if count == 3:
                    new_grid[i][j] = '#'

    return new_grid

def print_grid(grid):
    for row in grid:
        print("".join(row))

def how_many_on(grid):
    count = 0
    for row in grid:
        count += row.count("#")
    return count

for i in range(step_count):
    grid = step(grid)

print_grid(grid)
print(how_many_on(grid))


grid = open(input).read().splitlines()
grid = list(map(list, grid))

grid[0][0] = "#"
grid[0][len(grid[0]) - 1] = "#"
grid[len(grid) - 1][0] = "#"
grid[len(grid) - 1][len(grid[len(grid) - 1]) - 1] = "#"

for i in range(step_count):
    grid = step_corner(grid)

print_grid(grid)
print(how_many_on(grid))
