input = "day2"

reports = []
for report in open(input, "r").readlines(): 
  reports.append(list(map(int, report.split())))

def pairwise(iterable):
    iterator = iter(iterable)
    a = next(iterator, None)

    for b in iterator:
        yield a, b
        a = b

def isSafe(report: list[int]) -> bool:
  wasDown = None
  for x,y in pairwise(report):
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
  if (isSafe(report)): return True

  for index in range(len(report)):
    newReport = report.copy()
    newReport.pop(index)
    if (isSafe(newReport)): return True
  
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