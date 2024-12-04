input = "day4"

lines = open(input, "r").read().splitlines()

rowCount = len(lines)
colCount = len(lines[0])

# def hasXMASSnake(row, col, match):
#   count = 0
#   for nextRow in range(row if row == 0 else row - 1, row + 1 if row == rowCount - 1 else row + 2):
#     for nextCol in range(col if col == 0 else col - 1, col + 1 if col == colCount - 1 else col + 2):
#       if row == nextRow & col == nextCol: continue
#       char = lines[nextRow][nextCol]
#       if char == match: return 1
#       if match[0] == char:
#         count += hasXMASSnake(nextRow, nextCol, match[1:])
  
#   return count

def hasXMASDir(row, col, dirR, dirC, match):
  nextRow = row + dirR
  nextCol = col + dirC
  if 0 > nextRow or nextRow > rowCount - 1 or 0 > nextCol or nextCol > colCount - 1: return False
  char = lines[nextRow][nextCol]
  if char == match: return True
  if match[0] == char:
    return hasXMASDir(nextRow, nextCol, dirR, dirC, match[1:])
  return False

def hasMASDiag(row, col):
  def hasMas(d):
    return d == 'MAS' or d == 'SAM'

  diag1 = [lines[row][col], lines[row+1][col+1], lines[row+2][col+2]]
  diag2 = [lines[row][col+2], lines[row+1][col+1], lines[row+2][col]]

  return hasMas("".join(diag1)) and hasMas("".join(diag2))



def partOne():
  search = 'XMAS'
  count = 0
  for row in range(len(lines)):
    for col in range(len(lines[row])):
      if (lines[row][col] != search[0]): continue
      for dirR in [-1,0,1]:
        for dirC in [-1,0,1]:
          count += hasXMASDir(row, col, dirR, dirC, search[1:])

  print(count)

def partTwo():
  count = 0
  for row in range(len(lines) - 2):
    for col in range(len(lines[row]) -2):
      count += hasMASDiag(row, col)

  print(count)

# print(hasMASDiag(0, 1))
# partOne()
partTwo()