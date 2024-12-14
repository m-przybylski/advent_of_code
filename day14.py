import re
import copy

input = "day14"

cols = 101
rows = 103

def printRobots(robots):
  for i in range(rows):
    c = []
    for j in range(cols):
      found = False
      for robot, v in robots:
        col, row = robot
        if col == j and row == i:
          found = True
          break
      if found:
        c.append('#')
      else:
        c.append('.')
    print("".join(c))

def partOne():
  quadrant = [0, 0, 0, 0]
  for line in open(input).read().splitlines():

    def move(p, v):
      pCol, pRow = p
      vCol, vRow = v

      pCol = (pCol + vCol) % cols
      pRow = (pRow + vRow) % rows

      return (pCol, pRow)

    pCol, pRow, vCol, vRow = map(int, re.findall(r"-?\d+", line))
    position = (pCol, pRow)
    velocity = (vCol, vRow)

    for i in range(100):
      position = move(position, velocity)

    if position[0] < cols // 2 and position[1] < rows // 2:
      quadrant[0] += 1
    if position[0] < cols // 2 and position[1] > rows // 2:
      quadrant[1] += 1
    if position[0] > cols // 2 and position[1] < rows // 2:
      quadrant[2] += 1
    if position[0] > cols // 2 and position[1] > rows // 2:
      quadrant[3] += 1

  total = 1

  for val in quadrant:
    total = total * val

  print(total)

def partTwo():
  robots = []
  for line in open(input).read().splitlines():
    pCol, pRow, vCol, vRow = map(int, re.findall(r"-?\d+", line))
    position = (pCol, pRow)
    velocity = (vCol, vRow)
    robots.append((position, velocity))

  def move(p, v):
    pCol, pRow = p
    vCol, vRow = v

    pCol = (pCol + vCol) % cols
    pRow = (pRow + vRow) % rows

    return (pCol, pRow)

  robots_at_tree = None
  for i in range(1, 10000):
    for r in range(len(robots)):
      robot, velocity = robots[r]
      newPos = move(robot, velocity)
      robots[r] = (newPos, velocity)

    # find a line of 20
    tree = {}
    for position, velocity in robots:
      _, row = position
      if row not in tree:
        tree[row] = [position]
      else:
        tree[row].append(position)
      
    for row, r in tree.items():
      if len(r) > 30:
        r.sort(key=lambda a: a[0])
        count = 1
        previous = r[0]
        for robot in r:
          if previous[0] + 1 == robot[0]:
            count += 1
          else:
            count = 1
          previous = robot
        if count > 10:
          robots_at_tree = copy.deepcopy(robots)
          break
    else:
      continue
    break


  printRobots(robots_at_tree)
  print(i)


partOne()
# 225648864
partTwo()
# 7847
