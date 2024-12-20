input = "day20"

grid = [list(row) for row in open(input).read().splitlines()]
rows = len(grid)
cols = len(grid[0])

for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if col == "S":
            break
    else:
        continue
    break


def getPath(pos: tuple, path: list):
    seen = set()
    for p in path: seen.add(p)
    new_path = path[::]
    r, c = pos
    new_path.append((r, c))
    seen.add(pos)
    while grid[r][c] != "E":
        for new_r, new_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (new_r, new_c) in seen:
                continue
            if grid[new_r][new_c] == "." or grid[new_r][new_c] == "E":
                r, c = (new_r, new_c)
                new_path.append((r, c))
                seen.add((r, c))
                break
    return new_path


def build(pos, count):
  row,col = pos
  result = []
  for i in range(2, count + 1):
      inner = []
      inner.append((row + count, col))
      inner.append((row - count, col))
      for i in range(1, count):
        inner.append((row + i, col - (count - i)))
        inner.append((row - i, col - (count - i)))
        inner.append((row + i, col + (count - i)))
        inner.append((row - i, col + (count - i)))
      inner.append((row, col + count))
      inner.append((row, col - count))
      result.append(inner)

  return [element for sublist in result for element in sublist]

original_track = getPath((r, c), [])
original_len = len(original_track)
cheats = []

for i, step in enumerate(original_track):
    new_path = original_track[:i + 1]
    r, c = step
    for new_r, new_c in build(step, 2):
        if (new_r, new_c) not in original_track: continue
        cheat = i + 2 + original_len - original_track.index((new_r, new_c))

        if cheat < original_len:
          cheats.append(cheat)

saves = {}
for cheat in cheats:
    dif = original_len - cheat
    if dif not in saves:
        saves[dif] = 1
    else:
        saves[dif] += 1

print(sum(count if save >= 100 else 0 for save, count in saves.items()))

for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if col == "S":
            break
    else:
        continue
    break

dists = [[-1] * cols for _ in range(rows)]
dists[r][c] = 0

while grid[r][c] != 'E':
    for nr, nc in [(r+1,c), (r-1,c),(r,c+1),(r,c-1)]:
        if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
        if grid[nr][nc] == '#': continue
        if dists[nr][nc] != -1: continue
        dists[nr][nc] = dists[r][c] + 1
        r = nr
        c = nc

count = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '#': continue
        for radius in range(2,21):
          for dr in range(radius + 1):
              dc = radius - dr
              for nr, nc in {(r + dr, c + dc), (r + dr, c - dc), (r - dr, c + dc), (r - dr, c - dc)}:
                if nr < 0 or nc < 0 or nr >= rows or nc >= rows: continue
                if grid[nr][nc] == '#': continue
                if dists[r][c] - dists[nr][nc] >= 100 + radius: count += 1

print(count)
