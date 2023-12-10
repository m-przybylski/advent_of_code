from itertools import cycle
import math


input = "input/day8"

class Walk:
    def __init__(self, path, map, start) -> None:
        self.path = path
        self.map = map
        self.currentLocation = start

    def __str__(self) -> str:
        return self.path + "\n" + "\n".join([f"{self.map[key]}" for key in self.map])
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.currentLocation == "ZZZ":
            raise StopIteration
        
        if self.index == len(self.path):
            self.index = 0
                    
        currentLocation = self.currentLocation
        dir = self.path[self.index]
        newLocation = self.map[currentLocation][dir]
        self.index += 1
        self.currentLocation = newLocation
        return f"from: {currentLocation} with dir: {dir} to: {newLocation}"


def lineToNode(line):
    return { "source": line[0:3], "L" : line[7:10], "R": line[12:15] }

def parseData():
    file = open(input, "r")
    content = file.read().split("\n")
    path = content[0]
    del content[0:1]
    map = [lineToNode(line) for line in content if line != ""]
    dic = {}
    for node in map:
        dic[node["source"]] = node

    return (path, dic)


def part1():
    path, map = parseData()

    walk = Walk(path, map, "AAA")

    x = iter(walk)
    count = 0
    for _ in x:
        count +=1

    print(count)

def part2():
    def solve(current):
        for idx, dir in enumerate(cycle(path)):
            if current[-1] == "Z":
                return idx
            current = map[current][dir]

    path, map = parseData()
    starts = [k for k in map.keys() if k[-1] == "A"]

    return math.lcm(*[solve(s) for s in starts])

# 11309
# print(part1())

# 13740108158591
# print(part2())

for i in range(13740108158591):
    pass
