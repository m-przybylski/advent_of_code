from collections import deque

input = 'input/day23'

def printPath(grid, path):
    for i, row in enumerate(grid):
        items = []
        for j, col in enumerate(row):
            if (i,j) in path: items.append("O")
            else: items.append(col)

        print("".join(items))

def partOne():
    grid = open(input).read().splitlines()
    start_points = [i for i, space in enumerate(grid[0]) if space == "."]
    q = deque()
    for start_point in start_points:
        current_location = (0, start_point)
        seen = set()
        seen.add(current_location)
        q.append((current_location, seen, [current_location]))
    
    paths = []
    while q:
        location, seen_for_path, current_path = q.popleft()
        for new_dx, new_dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            new_location = (location[0] + new_dx, location[1] + new_dy)
            x,y = new_location
            if (x < 0):
                continue
            if new_location[0] == len(grid):
                paths.append(current_path)
                continue
            if grid[x][y] == "#":
                continue
            if new_location in seen_for_path:
                continue
            if grid[x][y] == ".":
                seen_for_path.add(new_location)
                current_path.append(new_location)
                q.append((new_location, seen_for_path, current_path))
                continue
            if grid[x][y] == ">" and (new_dx, new_dy) == (0, 1):
                seen = seen_for_path.copy()
                seen.add(new_location)
                q.append((new_location, seen, [*current_path, new_location]))
                continue
            if grid[x][y] == "v" and (new_dx, new_dy) == (1, 0):
                seen = seen_for_path.copy()
                seen.add(new_location)
                q.append((new_location, seen_for_path, [*current_path, new_location]))
                continue

    longest_path = 0

    for path in paths:
        if len(path) > longest_path:
            longest_path = len(path)
            
    print(longest_path - 1)


def partTwo():
    grid = open(input).read().splitlines()
    start = (0, grid[0].index("."))
    end = (len(grid) - 1, grid[len(grid) - 1].index("."))

    points = [start, end]

    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if col == "#":
                continue
            neighbors = 0
            for new_row, new_col in [(row_index - 1, col_index), (row_index + 1, col_index), (row_index, col_index - 1), (row_index, col_index + 1)]:
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] != "#":
                    neighbors += 1
            if neighbors >= 3:
                points.append((row_index, col_index))            

    
    graph = {pt: {} for pt in points}

    for sr, sc in points:
        stack = [(0, sr, sc)]
        seen = {(sr, sc)}

        while stack:
            n, r, c = stack.pop()
            
            if n != 0 and (r, c) in points:
                graph[(sr, sc)][(r, c)] = n
                continue

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#" and (nr, nc) not in seen:
                    stack.append((n + 1, nr, nc))
                    seen.add((nr, nc))

    seen = set()

    def dfs(pt):
        if pt == end:
            return 0

        m = -float("inf")

        seen.add(pt)
        for nx in graph[pt]:
            if nx not in seen:
                m = max(m, dfs(nx) + graph[pt][nx])
        seen.remove(pt)

        return m

    print(dfs(start))

# 2166
partOne()

partTwo()