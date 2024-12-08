import itertools

input = 'day8'

antena_locations = dict[str, list[(int, int)]]()
antena_map = [list(r) for r in open(input).read().splitlines()]
grid_r = len(antena_map)
grid_c = len(antena_map[0])

antinodes = set()

for r in range(grid_r):
  for c in range(grid_c):
    if antena_map[r][c] != '.':
      if antena_map[r][c] in antena_locations.keys():
        antena_locations.get(antena_map[r][c]).append((r,c))
      else:
        antena_locations[antena_map[r][c]] = [(r, c)]

def partOne():
  for antena_location in antena_locations.values():
    for (r1, c1), (r2, c2) in itertools.permutations(antena_location, 2):
      ri1 = r2 + r2 - r1
      ci1 = c2 + c2 - c1
      if (ri1 >= 0 and ri1 < grid_r and ci1 >= 0 and ci1 < grid_c): antinodes.add((ri1, ci1))
      ri2 = r1 + r1 - r2
      ci2 = c1 + c1 - c2
      if (ri2 >= 0 and ri2 < grid_r and ci2 >= 0 and ci2 < grid_c): antinodes.add((ri2, ci2))

  print(len(antinodes))
  
def partTwo():
  for antena_location in antena_locations.values():
    for (r1, c1), (r2, c2) in itertools.permutations(antena_location, 2):
      antinodes.add((r1, c1))
      antinodes.add((r2, c2))
      dr1 = r2 - r1
      dc1 = c2 - c1
      ri1 = r2 + dr1
      ci1 = c2 + dc1
      while True:
        if (ri1 >= 0 and ri1 < grid_r and ci1 >= 0 and ci1 < grid_c): 
          antinodes.add((ri1, ci1))
          ri1 = ri1 + dr1
          ci1 = ci1 + dc1
        else: break

      dr2 = r1 - r2
      dc2 = c1 - c2
      ri2 = r1 + dr2
      ci2 = c1 + dc2
      while True:
        if (ri2 >= 0 and ri2 < grid_r and ci2 >= 0 and ci2 < grid_c): 
          antinodes.add((ri2, ci2))
          ri2 = ri2 + dr2
          ci2 = ci2 + dc2

        else: break

  print(len(antinodes))
  

partOne()
partTwo()