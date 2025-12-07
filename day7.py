input = 'day7'

lines = [list(line.strip()) for line in open(input, 'r').readlines()]

beams = set()
start_index = None
for index, location in enumerate(lines.pop(0)):
  if location == 'S':
    beams.add(index)
    start_index = index
    break

def part_one():
  splits = 0
  for line in lines:
    for index, symbol in enumerate(line):
      if index not in beams:
        continue
      if symbol == "^":
        beams.remove(index)
        beams.add(index + 1)
        # line[index + 1] = '|'
        beams.add(index - 1)
        # line[index - 1] = '|'
        splits += 1
      # if symbol == '.':
      #   line[index] = '|'

  print(splits)


def part_two():
  cache = {}
  
  def solve(row, column):
      if (row, column) in cache:
         return cache[(row, column)]
      
      if row >= len(lines): 
        cache[(row, column)] = 1
        return 1
      
      if lines[row][column] == ".":
          result = solve(row + 1, column)
          cache[(row, column)] = result
          return result
      elif lines[row][column] == "^":
          result = solve(row, column - 1) + solve(row, column + 1)
          cache[(row, column)]  = result
          return result

  print(solve(0, start_index))

part_one()
part_two()