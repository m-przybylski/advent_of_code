import heapq
from collections import deque

input = 'day16'

grid = list(line for line in open(input).read().splitlines())

rows = len(grid)
cols = len(grid[0])
for r in range(rows):
  for c in range(cols):
    if grid[r][c] == 'S':
      break
  else:
    continue
  break

sr = r
sc = c

def partOne():
  pos = [(0, sr, sc, 0, 1)]
  seen = {(sr, sc, 0, 1)}

  cheapest = None
  while pos:
    cost, r, c, dr, dc = heapq.heappop(pos)
    seen.add((r, c, dr, dc))
    if grid[r][c] == 'E':
      cheapest = cost
      break
    # move forward
    new_cost = cost + 1
    new_r = r + dr
    new_c = c + dc
    new_dr = dr
    new_dc = dc
    if not (grid[new_r][new_c] == "#" or (new_r, new_c, new_dr, new_dc) in seen):
      heapq.heappush(pos, (new_cost, new_r, new_c, new_dr, new_dc))
    # rotate right
    new_cost = cost + 1000
    new_r = r
    new_c = c
    new_dr = dc
    new_dc = dr * -1
    if not (grid[new_r][new_c] == "#" or (new_r, new_c, new_dr, new_dc) in seen):
      heapq.heappush(pos, (new_cost, new_r, new_c, new_dr, new_dc))
    
    # rotate left
    new_cost = cost + 1000
    new_r = r
    new_c = c
    new_dr = dc * -1
    new_dc = dr 
    if not (grid[new_r][new_c] == "#" or (new_r, new_c, new_dr, new_dc) in seen):
      heapq.heappush(pos, (new_cost, new_r, new_c, new_dr, new_dc))

  print(cheapest)

def partTwo():
  pq = [(0, sr, sc, 0, 1)]
  lowest_cost = {(sr, sc, 0, 1): 0}
  backtrack = {}
  best_cost = float("inf")
  end_states = set()

  while pq:
    cost, r, c, dr, dc = heapq.heappop(pq)
    if cost > lowest_cost.get((r, c, dr, dc), float("inf")): continue
    if grid[r][c] == "E":
      if cost > best_cost: break
      best_cost = cost
      end_states.add((r, c, dr, dc))
    for new_cost, nr, nc, ndr, ndc in [(cost + 1, r + dr, c + dc, dr, dc), (cost + 1000, r, c, dc, -dr), (cost + 1000, r, c, -dc, dr)]:
      if grid[nr][nc] == "#": continue
      lowest = lowest_cost.get((nr, nc, ndr, ndc), float("inf"))
      if new_cost > lowest: continue
      if new_cost < lowest:
        backtrack[(nr, nc, ndr, ndc)] = set()
        lowest_cost[(nr, nc, ndr, ndc)] = new_cost
      backtrack[(nr, nc, ndr, ndc)].add((r, c, dr, dc))
      heapq.heappush(pq, (new_cost, nr, nc, ndr, ndc))

  states = deque(end_states)
  seen = set(end_states)

  while states:
      key = states.popleft()
      for last in backtrack.get(key, []):
          if last in seen: continue
          seen.add(last)
          states.append(last)
  print(len({(r, c) for r, c, _, _ in seen}))

partOne()
partTwo()