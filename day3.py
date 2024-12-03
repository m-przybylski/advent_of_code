import re

input = "day3"

instructions = open(input, "r").read()
def partOne():
  count = 0
  for a in re.finditer("mul\\(([0-9]){1,3},([0-9]){1,3}\\)", instructions):
    for x,y, in [list(map(int, instructions[a.start()+4:a.end()-1].split(",")))]:
      count += x * y

  print(count)

def partTwo():  
  count = 0
  is_counting = True
  for a in re.finditer("mul\\(([0-9]){1,3},([0-9]){1,3}\\)|do\\(\\)|don't\\(\\)", instructions):
    instruction = instructions[a.start():a.end()]
    if (instruction == "do()"):
      is_counting = True; continue
    if (instruction == "don't()"):
      is_counting = False; continue
    for x,y, in [list(map(int, instructions[a.start()+4:a.end()-1].split(",")))]:
      count += (x * y if is_counting else 0)

  print(count)


partOne()
partTwo()