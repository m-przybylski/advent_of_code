input = 'day6'

def part_one():
  rows = list((line.strip().split()) for line in open(input, 'r').readlines())
  operations = rows.pop()

  total = 0
  for i in range(len(operations)):
    result = 0
    if operations[i] == '*':
      result = 1
    for j in range(len(rows)):
      if operations[i] == '*':
        result *= int(rows[j][i])
      if operations[i] == '+':
        result += int(rows[j][i])
    total += result
  print(total)

def part_two():
  rows = open(input, 'r').read().split("\n")
  operations = rows.pop().split()
  operation = operations.pop(0)
  total = 0
  result = 1 if operation == '*' else 0

  for i in range(len(rows[0])):
    number = ""
    for j in range(len(rows)):
      number += rows[j][i]
    try:
      if operation == '*':
        result *= int(number)
      if operation == '+':
        result += int(number)
    except:
      # move to next operation
      total += result
      operation = operations.pop(0)
      result = 1 if operation == '*' else 0
      continue

  total += result
    
  print(total)

part_one()
part_two()