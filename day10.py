input = 'day10'

grid = []
for i, row in enumerate(open(input).read().splitlines()):
  grid.append([])
  for char in row:
    grid[i].append(int(char) if char != '.' else -1)
rows = len(grid)
cols = len(grid[0])
trailhead_starts = []

for r, row in enumerate(grid):
  for c, col in enumerate(grid[r]):
    if col == 0:
      trailhead_starts.append((r, c))

def partOne():
  count = 0
  for trailhead_start in trailhead_starts:
    nines = set()
    def getTrainScore(pos, valid_tops):
      r, c = pos
      trail_height = grid[r][c]
      if trail_height == 9:
        valid_tops.add((r,c))
        return
      next_r = r + 1
      if next_r >= 0 and next_r < rows and trail_height + 1 == grid[next_r][c]:
        getTrainScore((next_r, c), valid_tops)
      next_r = r - 1
      if next_r >= 0 and next_r < rows and trail_height + 1 == grid[next_r][c]:
        getTrainScore((next_r, c), valid_tops)
      next_c = c + 1
      if next_c >= 0 and next_c < cols and trail_height + 1 == grid[r][next_c]:
        getTrainScore((r, next_c), valid_tops)
      next_c = c - 1
      if next_c >= 0 and next_c < cols and trail_height + 1 == grid[r][next_c]:
        getTrainScore((r, next_c), valid_tops)
    getTrainScore(trailhead_start, nines)
    count += len(nines)
  print(count)

  
def partTwo():
  count = 0
  for trailhead_start in trailhead_starts:
    nines = []
    def getTrainScore(pos, valid_tops):
      r, c = pos
      trail_height = grid[r][c]
      if trail_height == 9:
        valid_tops.append((r,c))
        return
      next_r = r + 1
      if next_r >= 0 and next_r < rows and trail_height + 1 == grid[next_r][c]:
        getTrainScore((next_r, c), valid_tops)
      next_r = r - 1
      if next_r >= 0 and next_r < rows and trail_height + 1 == grid[next_r][c]:
        getTrainScore((next_r, c), valid_tops)
      next_c = c + 1
      if next_c >= 0 and next_c < cols and trail_height + 1 == grid[r][next_c]:
        getTrainScore((r, next_c), valid_tops)
      next_c = c - 1
      if next_c >= 0 and next_c < cols and trail_height + 1 == grid[r][next_c]:
        getTrainScore((r, next_c), valid_tops)
    getTrainScore(trailhead_start, nines)
    count += len(nines)

  print(count)

partOne()
partTwo()