input = 'day12'

grid = [list(line) for line in open(input).read().splitlines()]

def partOne():
  plants = {}

  rows = len(grid)
  cols = len(grid[0])

  visited = set()
  groups = []

  for i, row in enumerate(grid):
    for j, col in enumerate(row):
      if col not in plants:
        plants[col] = []
      plants[col].append((i,j))

      if (i,j) in visited:
        continue
      group = set()
      
      def guildGroupForPlant(row_index, col_index, plant):
        if (row_index == 0 and col_index == 3):
          pass
        if (row_index, col_index) in visited or grid[row_index][col_index] != plant:
          return
        else:
          visited.add((row_index,col_index))

        next_col = col_index + 1
        next_row = row_index + 1
        prev_col = col_index - 1
        prev_row = row_index - 1

        neighbors = 0
        if next_col < cols and grid[row_index][next_col] == plant:
          neighbors += 1
          guildGroupForPlant(row_index, next_col, plant)
        if prev_col >= 0 and grid[row_index][prev_col] == plant:
          neighbors += 1
          guildGroupForPlant(row_index, prev_col, plant)
        if next_row < rows and grid[next_row][col_index] == plant:
          neighbors += 1
          guildGroupForPlant(next_row, col_index, plant)
        if prev_row >= 0 and grid[prev_row][col_index] == plant:
          neighbors += 1
          guildGroupForPlant(prev_row, col_index, plant)

        group.add((row_index, col_index, neighbors))

          
      guildGroupForPlant(i, j, col)
      groups.append(group)

  total = 0
  for group in groups:
    perimeter = 0
    for x,y,n in group:
      perimeter += 4 - n

    total += perimeter * len(group)

  print(total)

def partTwo():
  plants = {}

  rows = len(grid)
  cols = len(grid[0])

  visited = set()
  groups = []

  total = 0
  for i, row in enumerate(grid):
    for j, col in enumerate(row):
      if col not in plants:
        plants[col] = []
      plants[col].append((i,j))

      if (i,j) in visited:
        continue
      group = []
      size = []
      
      def buildGroupForPlant(row_index, col_index, plant):
        if (row_index == 0 and col_index == 3):
          pass
        if (row_index, col_index) in visited or grid[row_index][col_index] != plant:
          return
        else:
          visited.add((row_index,col_index))

        next_col = col_index + 1
        next_row = row_index + 1
        prev_col = col_index - 1
        prev_row = row_index - 1

        neighbors = 0
        fence = []
        if next_col < cols and grid[row_index][next_col] == plant:
          neighbors += 1
          buildGroupForPlant(row_index, next_col, plant)
        else:
          fence.append((row_index, col_index + 0.5))
          pass
        if prev_col >= 0 and grid[row_index][prev_col] == plant:
          neighbors += 1
          buildGroupForPlant(row_index, prev_col, plant)
        else:
          fence.append((row_index, col_index - 0.5))
        if next_row < rows and grid[next_row][col_index] == plant:
          neighbors += 1
          buildGroupForPlant(next_row, col_index, plant)
        else:
          fence.append((row_index + 0.5, col_index))
        if prev_row >= 0 and grid[prev_row][col_index] == plant:
          neighbors += 1
          buildGroupForPlant(prev_row, col_index, plant)
        else:
          fence.append((row_index - 0.5, col_index))
        
        size.append(1)
        if neighbors < 4:
          for f in fence:
            group.append(f)
      
      buildGroupForPlant(i, j, col)

      def fun(g):
        return g[0]*10000 + g[1]
      
      group.sort(key=fun)

      groups.append(group)
      sides = 1
      element = group[0]
      dirNext = {
        'up': (0,1),
        'right': (1,0),
        'down': (0,-1),
        'left': (-1,0)
      }
      dirRight = {
        'up': ('right', (0.5, 0.5)),
        'right': ('down', (0.5, -0.5)),
        'down': ('left', (-0.5, -0.5)),
        'left': ('up', (-0.5, 0.5))
      }
      dirLeft = {
        'up': ('left', (-0.5, 0.5)),
        'right': ('up', (0.5, 0.5)),
        'down': ('right', (0.5, -0.5)),
        'left': ('down', (-0.5, -0.5))
      }
      current_fance_dir = 'up'
      while len(group):
        group.remove(element)
        x, y = element
        rx, ry = dirRight[current_fance_dir][1]
        right_fence = (x + rx, y + ry)
        nx, ny = dirNext[current_fance_dir]
        next_element = (x + nx, y + ny)
        lx, ly = dirLeft[current_fance_dir][1]
        left_fence = (x + lx, y + ly)
        if right_fence in group:
          current_fance_dir = dirRight[current_fance_dir][0]
          element = right_fence
          sides += 1
        elif left_fence in group:
          current_fance_dir = dirLeft[current_fance_dir][0]
          element = left_fence
          sides += 1
        elif next_element in group:
          element = next_element
        elif len(group):
          element = group[0]
          sides += 1
          current_fance_dir = 'up'
        else: 
          break

      
      total += sides * sum(size)

  print(total)


partOne()
partTwo()
