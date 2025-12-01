input = "day1"

rotations =  list((line[0], int(line[1:len(line)-1])) for line in open(input, "r").readlines())

def partOne():
  count = 0
  current = 50
  for direction, step in rotations:
    step = step % 100
    if direction == 'L':
      current = current - step
      if current < 0:
        current = 100 + current
    else:
      current = current + step
      if current > 99:
        current = current - 100
    if current == 0:
      count += 1
  print(count)

def partTwo():
  count = 0
  current = 50
  for direction, step in rotations:
    count += int(step / 100)
    step = step % 100
    if direction == 'L':
      if current == 0:
        current = 100
      current = current - step
      if current < 0:
        current = 100 + current
        if current != 0:
          count += 1
        print(current, step, 'L')
    else:
      current = current + step
      if current > 99:
        current = current - 100
        if current != 0:
          count += 1
        print(current, step, 'R')
    if current == 0:
      print(current)
      count += 1
  print(count)

partOne()
partTwo()