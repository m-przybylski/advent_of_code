input = 'day4'

grid = list(list(line.strip()) for line in open(input, 'r').readlines())

def print_grid():
  for x in range(len(grid)):
    print("".join(grid[x]))

rolls_to_move = 0

def part_one():
  global rolls_to_move
  for x in range(len(grid)):
    for y in range(len(grid[x])):
      if grid[x][y] != '@':
        continue
      adjacent_rolls = 0
      for (d1, d2) in [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1), (1,0),(1,1)]:
        dx = x + d1
        dy = y + d2
        if dx < len(grid) and dx >= 0 and dy < len(grid[x]) and dy >= 0:
          if grid[dx][dy] == '@' or grid[dx][dy] == 'x':
            adjacent_rolls += 1
      if adjacent_rolls < 4:
        rolls_to_move += 1
        grid[x][y] = 'x'

  print(rolls_to_move)

def part_two():
  global rolls_to_move
  while True:
    roll_removed = False
    for x in range(len(grid)):
      for y in range(len(grid[x])):
        if grid[x][y] != '@':
          continue
        adjacent_rolls = 0
        for (d1, d2) in [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1), (1,0),(1,1)]:
          dx = x + d1
          dy = y + d2
          if dx < len(grid) and dx >= 0 and dy < len(grid[x]) and dy >= 0:
            if grid[dx][dy] == '@':
              adjacent_rolls += 1
        if adjacent_rolls < 4:
          rolls_to_move += 1
          grid[x][y] = 'x'
          roll_removed = True
    if roll_removed:
      continue
    break

  print(rolls_to_move)

part_one()
part_two()
