key_and_locks = open('day25').read().split("\n\n")

keys = []
locks = []

for key_or_lock in key_and_locks:
  pivot = list(zip(*key_or_lock.splitlines()))
  key_or_lock = key_or_lock.splitlines()
  is_lock = key_or_lock[0][0] == "#"
  
  heights = [row.count("#") -1 for row in pivot]
  if is_lock:
    locks.append(heights)
  else:
    keys.append(heights)


total = 0
for key in keys:
  for lock in locks:
    if all(key[i] + lock[i] <= 5 for i in range(len(key))):
      total += 1

print(total)