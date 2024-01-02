input = "1113122113"

        
def getNextLookAndSay(value = "1"):
    starts = []
    prev = None
    count = 0
    for i in range(len(value)):
        count += 1
        if (value[i] != prev):
            prev = value[i]
            starts.append((i, count))
            count = 0

    next = ""
    for idx, (start, _) in enumerate(starts):
        if (idx == len(starts) - 1):
            next += f"{(len(value) - start)}{value[start]}"
            continue
        next += f"{starts[idx + 1][1]}{value[start]}"
    
    return next

val = input
for i in range(40):
    val = getNextLookAndSay(val)

print(len(val))

for i in range(10):
    val = getNextLookAndSay(val)

print(len(val))
