import itertools

input = 'day7'

test = []

for line in open(input).read().splitlines():
  result, numbers = line.split(":")
  test.append((int(result), list(map(int, numbers.split()))))

def partOne():
  def isPossible(result , numbers):
    operators = itertools.product('*+', repeat=(len(numbers) - 1))

    for ops in operators:
      eq = numbers[0]
      for i in range(1, len(numbers)):
        eq = eq + numbers[i] if ops[i - 1] == "+" else eq * numbers[i]

      if (eq == result):
        return result
    
    return 0
  
  count = 0
  for equation in test:
    result , numbers = equation
    count += isPossible(result, numbers)

  print(count)


def partTwo():
  def isPossible(result , numbers):
    operators = itertools.product('*+|', repeat=(len(numbers) - 1))

    for ops in operators:
      eq = numbers[0]
      for i in range(1, len(numbers)):
        if ops[i - 1] == "+":
          eq = eq + numbers[i]
        elif ops[i - 1] == "*":
          eq = eq * numbers[i]
        else:
          eq = int(str(eq) + str(numbers[i]))
        

      if (eq == result):
        return result
    
    return 0
  
  count = 0
  for equation in test:
    result , numbers = equation
    count += isPossible(result, numbers)

  print(count)

partOne()
partTwo()

# isPossible(292, ['11', '6', '16', '20'])