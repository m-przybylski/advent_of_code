import copy

input = 'day6'

guard_map = open(input).read().splitlines()

start_positions = ["^", ">", "<", "v"]

directions = {
  "^": (-1, 0),
  ">": (0, 1),
  "v": (1, 0),
  "<": (0, -1),
}

turn = {
  (-1, 0): (0, 1),
  (0, 1): (1, 0),
  (1, 0): (0, -1),
  (0, -1): (-1, 0)
}

def getStartPosition():
  for i in range(len(guard_map)):
    for j in range(len(guard_map[0])):
      if (guard_map[i][j] in start_positions):
        return (i, j, guard_map[i][j])

start_position = getStartPosition()

def partOne():
  visited_locations = set()
        
  def outOfMap(position):
    x,y = position
    return True if (x > len(guard_map) -1 or y > len(guard_map) -1 or x < 0 or y < 0) else False
  
  def move(position, velocity):
    x,y = position
    dx, dy = velocity
    return (x+dx, y+dy)
  
  def getNextPosition(position, velocity):
    x1, y1 = move(position, velocity)
    if outOfMap((x1, y1)): return (None, None)
    if guard_map[x1][y1] == "#": return (position, turn[velocity])
    return ((x1, y1), velocity)


  (x, y, dir) = start_position
  velocity = directions[dir]
  current_position = (x,y)
  visited_locations.add(current_position)

  while (True):
    next_position, next_velocity = getNextPosition(current_position, velocity)
    if next_position == None: break
    visited_locations.add(next_position)
    current_position = next_position
    velocity = next_velocity

  print(len(visited_locations))
  return visited_locations

def printMap(map_to_print):
  for i in range(len(map_to_print)):
    print(map_to_print[i])

def partTwo(points_on_path):
  loops = 0
  for i in range(len(guard_map)):
    for j in range(len(guard_map[0])):
      if (i,j) not in points_on_path or guard_map[i][j] != '.': continue
      visited_locations = set()
      
      def outOfMap(position):
        x,y = position
        return True if (x > len(guard_map) -1 or y > len(guard_map) -1 or x < 0 or y < 0) else False
      
      def move(position, velocity):
        x,y = position
        dx, dy = velocity
        return (x+dx, y+dy)
      
      def getNextPosition(position, velocity):
        x1, y1 = move(position, velocity)
        if outOfMap((x1, y1)): return (None, None)
        # Rotate
        if guard_map[x1][y1] == "#" or (x1 == i and y1 == j): 
          return (position, turn[velocity])
        return ((x1, y1), velocity)

      (x, y, dir) = start_position
      velocity = directions[dir]
      current_position = (x,y)
      visited_locations.add((current_position, velocity))

      while (True):
        next_position, next_velocity = getNextPosition(current_position, velocity)
        # Check if out of map
        if next_position == None: 
          break
        # Check if in da loop
        if ((next_position, next_velocity)) in visited_locations: 
          loops += 1
          break

        visited_locations.add((next_position, next_velocity))
        current_position = next_position
        velocity = next_velocity
  print(loops)

visited_locations = partOne()
partTwo(visited_locations)
