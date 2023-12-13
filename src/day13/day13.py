input = 'input/day13'

def parseData():
    fields = open(input, "r").read().split("\n\n")
    return [x.splitlines() for x in fields]

def getSize(field):
    def findSplit(fld) -> int:
        sameRowIndex = []
        for i in range(len(fld) - 1):
            if fld[i] == fld[i + 1]:
                sameRowIndex.append(i+1)
        return sameRowIndex
    
    def checkIfMirror(fld, index) -> bool:
        left = fld[:index][::-1]
        right = fld[index:]

        length = min(len(left), len(right))
        left = left[:length]
        right = right[:length]

        return left == right


    splits = findSplit(field)
    for split in splits:
        isMirror = checkIfMirror(field, split)
        if (isMirror):
            return split * 100
    
    field = list(map("".join, zip(*field)))
    splits = findSplit(field)
    for split in splits:
        isMirror = checkIfMirror(field, split)
        if (isMirror):
            return split

    assert 1 != 1


def getSizeWithSmuge(field):
    def findSplit(fld) -> int:
        sameRowIndex = []

        for i in range(len(fld) - 1):
            if fld[i] == fld[i + 1] or sum(1 for c1, c2 in list(zip(fld[i], fld[i + 1])) if c1 != c2) == 1:
                sameRowIndex.append(i+1)
        return sameRowIndex
    
    def checkIfMirror(fld, index) -> bool:
        left = fld[:index][::-1]
        right = fld[index:]

        length = min(len(left), len(right))
        left = left[:length]
        right = right[:length]

        return sum(sum(1 for c1,c2 in zip(r1,r2) if c1 != c2) for r1, r2 in zip(left, right)) == 1

    splits = findSplit(field)
    for split in splits:
        isMirror = checkIfMirror(field, split)
        if (isMirror):
            return split * 100
    
    field = list(map("".join, zip(*field)))
    splits = findSplit(field)
    for split in splits:
        isMirror = checkIfMirror(field, split)
        if (isMirror):
            return split

    assert 1 != 1

def partOne():
    fields = parseData()
    count = 0
    for field in fields:
        count += getSize(field)
    print(count)

def partTwo():
    fields = parseData()
    count = 0
    for field in fields:
        count += getSizeWithSmuge(field)
    print(count)

#31265
partOne()

# 39359
partTwo()
