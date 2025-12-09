boxes = [tuple(map(int, line.strip().split(','))) for line in open('day8', 'r').readlines()]

distances = []
for i, a in enumerate(boxes):
  for j, b in enumerate(boxes):
    if i >= j: continue
    distance = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2
    distances.append((distance, (a, b)))

distances.sort()

def part_one():
  groups = []
  connections = 1000
  connection_made = 0
  current_distance = 0
  while connection_made < connections:
    j1_group = None
    j2_group = None
    _, (j1, j2) = distances[current_distance]
    for group in groups:
      if j1 in group and j2 in group:
        j1_group = j2_group = group
        break
      if j1 in group:
        j1_group = group
        continue
      if j2 in group:
        j2_group = group
        continue
    if j1_group and j2_group and j1_group != j2_group:
      groups.append(j1_group.union(j2_group))
      groups.remove(j1_group)
      groups.remove(j2_group)
    elif j1_group and j2_group and j1_group == j2_group:
      pass
    elif j1_group:
      j1_group.add(j2)
    elif j2_group:
      j2_group.add(j1)

    if j1_group is None and j2_group is None:
      groups.append(set([j1, j2]))
    connection_made += 1
    current_distance += 1
    
  groups.sort(key=len)
  print(len(groups[-1]) * len(groups[-2]) * len(groups[-3]))

def part_two():
  groups = []
  connection_made = 0
  current_distance = 0
  while connection_made < len(boxes) - 1:
    j1_group = None
    j2_group = None
    _, (j1, j2) = distances[current_distance]
    for group in groups:
      if j1 in group and j2 in group:
        j1_group = j2_group = group
        connection_made -= 1
        break
      if j1 in group:
        j1_group = group
        continue
      if j2 in group:
        j2_group = group
        continue
    if j1_group and j2_group and j1_group != j2_group:
      groups.append(j1_group.union(j2_group))
      groups.remove(j1_group)
      groups.remove(j2_group)
    elif j1_group and j2_group and j1_group == j2_group:
      pass
    elif j1_group:
      j1_group.add(j2)
    elif j2_group:
      j2_group.add(j1)

    if j1_group is None and j2_group is None:
      groups.append(set([j1, j2]))
    connection_made += 1
    current_distance += 1
    
  groups.sort(key=len)
  print(groups[-1], groups[-2], groups[-3])
  print(len(groups[-1]) * len(groups[-2]) * len(groups[-3]))

part_one()
part_two()

#  This is not mine code and I do not understand it!
# import sys
# from functools import cache
# from collections import defaultdict, Counter, deque

# D = open('day8', 'r').read()

# P = []
# for line in D.splitlines():
#     x,y,z = [int(x) for x in line.split(',')]
#     P.append((x,y,z))

# D = []
# for i,(x1,y1,z1) in enumerate(P):
#     for j,(x2,y2,z2) in enumerate(P):
#         distance = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
#         if i>j:
#             D.append((distance, i, j))
# D = sorted(D)

# UF = {i: i for i in range(len(P))}
# def find(x):
#     if x==UF[x]:
#         return x
#     UF[x] = find(UF[x])
#     return UF[x]
# def mix(x,y):
#     UF[find(x)] = find(y)

# connections = 0
# for t,(_d, i, j) in enumerate(D):
#     if t==1000:
#         SZ = defaultdict(int)
#         for x in range(len(P)):
#             SZ[find(x)] += 1
#         S = sorted(SZ.values())
#         print(S[-1]* S[-2]* S[-3])
#     if find(i) != find(j):
#         connections += 1
#         if connections==len(P)-1:
#             print(P[i][0]*P[j][0])
#         mix(i,j)