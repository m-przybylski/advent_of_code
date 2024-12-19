lines = open('day19').read().splitlines()

patterns = set(lines[0].split(", "))
maxlen = max(map(len, patterns))

def can_obtain(design):
    if design == "": return True
    for i in range(min(len(design), maxlen) + 1):
        if design[:i] in patterns and can_obtain(design[i:]):
            return True
    return False

print(sum(1 if can_obtain(design) else 0 for design in lines[2:]))


cache = {}

def num_possibilities(design):
    if design in cache:
        return cache[design]
    
    if design == "": return 1
    count = 0
    for i in range(min(len(design), maxlen) + 1):
        if design[:i] in patterns:
            count += num_possibilities(design[i:])

    cache[design] = count
    return count

print(sum(num_possibilities(design) for design in lines[2:]))