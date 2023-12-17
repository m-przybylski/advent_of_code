from heapq import heappop, heappush

input = "input/day17"

grid = [list(map(int, line.strip())) for line in open(input).read().splitlines()]

def partOne():
    seen = set()
    queue = [(0,0,0,0,0,0)]

    while queue:
        heatLoss, rowId, colId, rowV, colV, length = heappop(queue)

        if rowId == len(grid) -1 and colId == len(grid[0]) -1:
            print(heatLoss)
            break

        if (rowId, colId, rowV, colV, length) in seen:
            continue

        seen.add((rowId, colId, rowV, colV, length))

        if length < 3 and (rowV, colV) != (0,0):
            newRow = rowId + rowV
            newCol = colId + colV
            if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]):
                heappush(queue, (heatLoss + grid[newRow][newCol], newRow, newCol, rowV, colV, length + 1))

        for newRowV, newColV in [(0,1), (0,-1), (1,0), (-1,0)]:
            if (newRowV, newColV) != (rowV, colV) and (newRowV, newColV) != (rowV * -1, colV * -1):
                newRow = rowId + newRowV
                newCol = colId + newColV
                if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]):
                    heappush(queue, (heatLoss + grid[newRow][newCol], newRow, newCol, newRowV, newColV, 1))


def partTwo():
    seen = set()
    queue = [(0,0,0,0,0,0)]

    while queue:
        heatLoss, rowId, colId, rowV, colV, length = heappop(queue)

        if rowId == len(grid) -1 and colId == len(grid[0]) -1 and length >= 4:
            print(heatLoss)
            break

        if (rowId, colId, rowV, colV, length) in seen:
            continue

        seen.add((rowId, colId, rowV, colV, length))

        if length < 10 and (rowV, colV) != (0,0):
            newRow = rowId + rowV
            newCol = colId + colV
            if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]):
                heappush(queue, (heatLoss + grid[newRow][newCol], newRow, newCol, rowV, colV, length + 1))

        
        if length >= 4 or (rowV, colV) == (0,0):
            for newRowV, newColV in [(0,1), (0,-1), (1,0), (-1,0)]:
                if (newRowV, newColV) != (rowV, colV) and (newRowV, newColV) != (rowV * -1, colV * -1):
                    newRow = rowId + newRowV
                    newCol = colId + newColV
                    if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]):
                        heappush(queue, (heatLoss + grid[newRow][newCol], newRow, newCol, newRowV, newColV, 1))
# 742
partOne()

partTwo()
