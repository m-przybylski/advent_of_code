input = 'day15'

water, moves = open(input).read().split("\n\n")
moves = "".join(map(str.strip, moves.splitlines()))

rows = len(water.splitlines())
cols = len(water.splitlines()[0])

def partOne():
  boxes = []
  walls = []
  pos = None

  for r, row in enumerate(water.splitlines()):
    for c, col in enumerate(row):
      if col == 'O':
        boxes.append((r, c))
      elif col == '#':
        walls.append((r, c))
      elif col == '@':
        pos = (r,c)
      else:
        continue

  def clear_position(pos, dir):
    r,c = pos
    if r < 0 or r >= rows or c < 0 or c >= cols:
      return False
    
    if pos in walls:
      return False
    if pos in boxes:
      new_pos = (pos[0] + dir[0], pos[1] + dir[1])
      if clear_position(new_pos, dir):
        box_index = boxes.index(pos)
        boxes[box_index] = new_pos
        return True
      else:
        return False
    else:
      return True

  for move in moves:
    if move == '^':
      dir = (-1, 0)
    elif move == '<':
      dir = (0, -1)
    elif move == 'v':
      dir = (1, 0)
    elif move == '>':
      dir = (0, 1)
    else:
      print(move)
      raise Exception("Invalid input")
    
    # possible next position
    new_pos = (pos[0] + dir[0], pos[1] + dir[1])
    if clear_position(new_pos, dir):
      pos = new_pos

  gps = 0
  for box in boxes:
    gps += 100 * box[0] + box[1]

  print(gps)

def partTwo():
  grid = []
  subs = {
    "#": "##",
    ".": "..",
    "O": "[]",
    "@": "@."
  }

  grid = [list("".join(subs[char] for char in line)) for line in water.splitlines()]
  rows = len(grid)
  cols = len(grid[0])

  for r, row in enumerate(grid):
    for c, col in enumerate(row):
      if col == '@':
        pos = (r,c)
        break
    else:
      continue
    break

  for move in moves:
    dr = {"^": -1, "v": 1}.get(move, 0)
    dc = {"<": -1, ">": 1}.get(move, 0)
    targets = [(r, c)]
    go = True
    for cr, cc in targets:
        nr = cr + dr
        nc = cc + dc
        if (nr, nc) in targets: continue
        char = grid[nr][nc]
        if char == "#":
            go = False
            break
        if char == "[":
            targets.append((nr, nc))
            targets.append((nr, nc + 1))
        if char == "]":
            targets.append((nr, nc))
            targets.append((nr, nc - 1))
    if not go: continue
    copy = [list(row) for row in grid]
    grid[r][c] = "."
    grid[r + dr][c + dc] = "@"
    for br, bc in targets[1:]:
        grid[br][bc] = "."
    for br, bc in targets[1:]:
        grid[br + dr][bc + dc] = copy[br][bc]
    r += dr
    c += dc

  print(sum(100 * r + c for r in range(rows) for c in range(cols) if grid[r][c] == "["))

partOne()
partTwo()