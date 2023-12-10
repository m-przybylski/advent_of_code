input = "input/day9"

def all(arr, val):
    for el in arr:
        if el != val:
            return False
    
    return True

def parseData():
    lines = open(input, "r").read().split("\n")
    return [
        [ int(reading) for reading in line.split(" ")] 
        for line in lines
    ]

def part1():
    history = parseData()
    predictionSum = 0
    for line in history:
        data = [line]
        current = line
        while not all(current, 0):
            current = [ current[i+1] - current[i] for i in range(len(current) -1) ]
            data.append(current)
        
        prev = 0
        for i in range(len(data)-1, -1, -1):
            a = data[i][-1]
            data[i].append(prev + a)
            prev += a
        
        predictionSum += data[0][-1]

    return predictionSum

def part2():
    history = parseData()
    predictionSum = 0
    for line in history:
        data = [line]
        current = line
        while not all(current, 0):
            current = [ current[i+1] - current[i] for i in range(len(current) -1) ]
            data.append(current)
        
        prev = 0
        for i in range(len(data)-1, -1, -1):
            a = data[i][0]
            data[i].append(a - prev)
            prev = a - prev
        
        predictionSum += data[0][-1]

    return predictionSum
    
# 1939607039
print(part1())

# 1041
print(part2())
        