input = "day1"

locations = list(map(list, zip(*[list(map(int, line.split())) for line in open(input, "r").readlines()])))
for locationIds in locations: locationIds.sort()

def partOne():
  print(sum(abs(left - right)for left, right in zip(*locations)))

def partTwo():
  left, right = locations
  print(sum(l * right.count(l) for l in left))

partOne()
partTwo()