input = "day2"

import itertools

get_start_and_stop = lambda x: (int(x[0]), int(x[1]))

product_ranges = list(get_start_and_stop(productRange.split('-')) for productRange in open(input, "r").read().strip().split(','))

def is_invalid(num):
  num_as_string = str(num)
  if len(num_as_string) % 2 != 0:
    return False
  if num_as_string[0:len(num_as_string) // 2] == num_as_string[len(num_as_string) // 2 : len(num_as_string)]:
    return True
  
  return False

def is_invalid_patterns(num):
  num_as_string = str(num)
  for i in range(1, len(num_as_string) // 2 + 1):
    if len(num_as_string) % i != 0:
      continue

    pattern = num_as_string[0:i]
    if num_as_string == ''.join((itertools.repeat(pattern, len(num_as_string) // len(pattern)))):
      return True

  return False 


def partOne():
  sum = 0
  for start, stop in product_ranges:
    for i in range(start, stop + 1):
      if is_invalid(i):
        sum += i
  print(sum)

def partTwo():
  sum = 0
  for start, stop in product_ranges:
    for i in range(start, stop + 1):
      if is_invalid_patterns(i):
        sum += i
  print(sum)

partOne()
partTwo()