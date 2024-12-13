import re
input = 'day13'

lines =  open(input).read().splitlines()

def partOne():
  machines = []
  for i in range(0, len(lines), 4):
    buttonA = list(map(int, [coordinate.split('+')[1] for coordinate in lines[i].split(": ")[1].split(", ")]))
    buttonB = list(map(int, [coordinate.split('+')[1] for coordinate in lines[i + 1].split(": ")[1].split(", ")]))
    prize = list(map(int, [coordinate.split('=')[1] for coordinate in lines[i + 2].split(": ")[1].split(", ")]))
    machines.append((buttonA, buttonB, prize))

  def canWin(machine):
    [xa, ya], [xb, yb], [xp, yp] = machine
    result = 0
    possible = []

    for i in range(101):
      if xa * i > xp or ya * i > yp: break
      if (xp - (xa * i)) % xb == 0 and (yp - (ya * i)) % yb == 0:
        targetBx = (xp - (xa * i)) // xb
        targetBy = (yp - (ya * i)) // yb
        if (targetBx == targetBy and targetBx <= 100):
          tokensA = i * 3
          tokensB = targetBx * 1
          possible.append(tokensA + tokensB)

    for tokens in possible:
      if result == 0 or tokens < result:
        result = tokens
    
    return result

  print(sum(canWin(machine) for machine in machines))

def partTwo():
  machines = []
  for i in range(0, len(lines), 4):
    buttonA = list(map(int, [coordinate.split('+')[1] for coordinate in lines[i].split(": ")[1].split(", ")]))
    buttonB = list(map(int, [coordinate.split('+')[1] for coordinate in lines[i + 1].split(": ")[1].split(", ")]))
    prize = list(map(int, [coordinate.split('=')[1] for coordinate in lines[i + 2].split(": ")[1].split(", ")]))
    prize = prize[0] + 10000000000000, prize[1] + 10000000000000
    machines.append((buttonA, buttonB, prize))

  def canWin(machine):
    [xa, ya], [xb, yb], [xp, yp] = machine
    
    B = ((xa*yp) - (ya*xp)) / ((xa*yb) - (ya * xb))
    if B.is_integer():
      A = (xp - (xb*B)) / xa
      if A.is_integer():
        return int(A) * 3 + int(B)
      
    return 0

  print(sum(canWin(machine) for machine in machines))

partOne()
partTwo()