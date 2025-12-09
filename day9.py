grid = [tuple(map(int, line.split(","))) for line in open("day9", 'r').readlines()]

def part_one():
  max_area = 0
  for i, [x1,y1] in enumerate(grid):
    for j, [x2,y2] in enumerate(grid):
      if i >= j: continue
      area = abs(x1 - x2 + 1) * abs(y1 - y2 + 1)
      max_area = max(area, max_area)
  print(max_area)

def part_two():
  edges = []
  n = len(grid)
  for i in range(n - 1):
    p1 = grid[i]
    p2 = grid[i + 1]
    edges.append((min(p1[0], p2[0]), min(p1[1], p2[1]), max(p1[0], p2[0]), max(p1[1], p2[1])))

  p_last = grid[-1]
  p_first = grid[0]
  edges.append((min(p_last[0], p_first[0]),min(p_last[1], p_first[1]),max(p_last[0], p_first[0]),max(p_last[1], p_first[1])))

  def does_intersect(min_x,min_y,max_x,max_y):
    for e_min_x, e_min_y, e_max_x, e_max_y in edges:
      if min_x < e_max_x and max_x > e_min_x and min_y < e_max_y and max_y > e_min_y:
        return True
    return False
  
  max_area = 0
  for i, p1 in enumerate(grid):
    for j, p2 in enumerate(grid):
      if i >= j: continue
      area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
      if max_area > area:
        continue
      min_x, max_x = (p1[0], p2[0]) if p1[0] < p2[0] else (p2[0], p1[0])
      min_y, max_y = (p1[1], p2[1]) if p1[1] < p2[1] else (p2[1], p1[1])

      if not does_intersect(min_x, min_y, max_x, max_y):
        max_area = area
      
  print(max_area)


part_one()
part_two()
