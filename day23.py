input = 'day23'

links = open(input).read().splitlines()

comps = {}

for link in links:
  l, r = link.split("-")
  if l not in comps: comps[l] = set()
  if r not in comps: comps[r] = set()
  comps[l].add(r)
  comps[r].add(l)

def partOne():

  groups = set()

  for s in comps:
    for d1 in comps[s]:
      for d2 in comps[d1]:
        if s != d2 and s in comps[d2]:
          groups.add(tuple(sorted([s, d1, d2])))

  print(len([s for s in groups if any(cn.startswith("t") for cn in s)]))

def partTwo():
  sets = set()

  def search(node, req):
    key = tuple(sorted(req))
    if key in sets: return
    sets.add(key)
    for neighbor in comps[node]:
      if neighbor in req: continue
      if not all(neighbor in comps[query] for query in req): continue
      search(neighbor, {*req, neighbor})

  for x in comps:
    search(x, {x})

  print(",".join(sorted(max(sets, key=len))))


partOne()
partTwo()