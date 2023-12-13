input = "input/day12"

cache = {}

def readLine(line):
    springs, nums = line.split()
    nums = list(map(int, nums.split(",")))
    return (springs, nums)

def count(config, nums):
    key = (config, tuple(nums))

    if key in cache:
        return cache[key]
    
    result = 0
    if config == "":
        return 1 if nums == [] else 0
    
    if nums == []:
        return 0 if "#" in config else 1
    
    if config[0] in ".?":
        result += count(config[1:], nums)

    if config[0] in "#?":
        if nums[0] <= len(config) and "." not in config[:nums[0]] and (nums[0] == len(config) or config[nums[0]] != "#"):
            result += count(config[nums[0] + 1:], nums[1:])

    cache[key] = result
    return result

def parseData():
    rows = list(map(lambda x: readLine(x), open(input, "r").read().splitlines()))
    return rows


def partOne():
    rows = parseData()
    outcomes = 0
    for config, nums in rows:
        outcomes += count(config, nums)

    print(outcomes)

def partTwo():
    rows = parseData()
    outcomes = 0
    for config, nums in rows:
        nums = nums * 5
        config = ((config + "?") * 5)[:-1]
        outcomes += count(config, nums)

    print(outcomes)

# 7350
partOne()

partTwo()