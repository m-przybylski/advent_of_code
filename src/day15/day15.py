from collections import OrderedDict

input = "input/day15"

def parseData():
    return open(input, "r").read().split(",")

def partOne():
    h = parseData()
    total = sum(list(map(calculateHash, h)))
    print(total)
    return total
    
def calculateHash(input: str) -> int:
    currentValue = 0
    for c in input:
        currentValue += ord(c)
        currentValue *= 17
        currentValue = currentValue % 256
    
    return currentValue

def partTwo():
    steps = parseData()
    boxes = [OrderedDict() for _ in range(256)]
    for step in steps:
        action = '-' if step[-1:][0] == '-' else '='
        label = step[:-2] if action == "=" else step[:-1]
        focalLength = step[-1:] if action == "=" else 0
        boxNumber = calculateHash(label)
        box = boxes[boxNumber]

        if (action == '-'):
            try:
                box.pop(label)
            except KeyError:
                pass

        else:
            box[label] = focalLength
    count = 0
    for boxId, box in enumerate(boxes):
        for lenseId, fl in enumerate(box.items()):
            count += (boxId + 1) * (lenseId + 1) * int(fl[1])
        
    print(count)



#513172
partOne()

#237806
partTwo()
