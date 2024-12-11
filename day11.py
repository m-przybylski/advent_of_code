input = 'day11'

stones = list(map(int, open(input).read().split()))

def partOne():
  partOneStones = stones.copy()
  iterations = 25
  for _ in range(iterations):
    newStones = []
    for stone in partOneStones:
      if stone == 0:
        newStones.append(1)
      elif len(str(stone)) % 2 == 0:
        stoneStr = str(stone)
        half = len(stoneStr) // 2
        left = stoneStr[:half]
        right = stoneStr[half:]
        newStones.append(int(left))
        newStones.append(int(right))
      else:
        newStones.append(stone * 2024)
    partOneStones = newStones

  print(len(partOneStones))

def partTwo():
  iterations = 75
  def count(stone, blinks):
    if blinks == 0:
      return 1
    if stone == 0:
      result = count(1, blinks - 1)
      return result

    if len(str(stone)) % 2 == 0:
        stoneStr = str(stone)
        half = len(stoneStr) // 2
        result = count(int(stoneStr[:half]), blinks - 1) + count(int(stoneStr[half:]), blinks - 1)
        return result

    return count(stone * 2024, blinks - 1)
  
  count = Memoize(count)
  result = sum(count(s, iterations) for s in stones)
  print(result)


class Memoize:
  def __init__(self, f):
      self.f = f
      self.memo = {}
  def __call__(self, *args):
      if not args in self.memo:
          self.memo[args] = self.f(*args)
      #Warning: You may wish to do a deepcopy here if returning objects
      return self.memo[args]


# partOne()
partTwo()