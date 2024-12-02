input = "day2"

reports = [list(map(int, report.split())) for report in open(input, "r").readlines()]

def isSafe(report: list[int]) -> bool:
  wasDown = None
  for x,y in zip(report[1:], report):
    if (x == y):
       return False

    diff = y - x
    
    if (abs(diff) > 3): return False
    if (wasDown == None):
      wasDown = True if diff < 0 else False
      continue

    if (wasDown != (True if diff < 0 else False)):
       return False    

  return True

def isSafeWithError(report: list[int]) -> bool:
  for index in range(len(report)):
    if (isSafe(report[:index] + report[index + 1:])): return True
  
  return False

def dayOne():
  count = 0
  for report in reports:
     if (isSafe(report)):
        count += 1
  print(count)

def dayTwo():
  count = 0
  for report in reports:
     if (isSafeWithError(report)):
        count += 1
  print(count)


dayOne()
dayTwo()