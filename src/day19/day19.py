input = "input/day19"

instructions, points = open(input).read().split("\n\n")
instructions = instructions.splitlines()
points = points.splitlines()
workflows = {}
result = {
    "A": [],
    "R": []
}

def str_to_dict(string):
    string = string.strip('{}')
    pairs = string.split(',')
    return {key: int(value) for key, value in (pair.split('=') for pair in pairs)}

def pipeShit(point, workflow_name = "in"):
    global workflows
    if (workflow_name in "AR"):
        result[workflow_name].append(point)
        return

    workflow = workflows[workflow_name]
    for rule in workflow:
        if ">" in rule:
            category, rest = rule.split(">")
            number, new_workflow_name = rest.split(":")

            if point[category] > int(number):
                return pipeShit(point, new_workflow_name)
        elif "<" in rule:
            category, rest = rule.split("<")
            number, new_workflow_name = rest.split(":")

            if point[category] < int(number):
                return pipeShit(point, new_workflow_name)
        else:
            return pipeShit(point, rule)
        
        

def parseWorkflow(instruction):
    name, rules = instruction[:-1].split("{")
    rules = rules.split(",")
    return (name, rules)

for instruction in instructions:
    parsedWorkflow = parseWorkflow(instruction)
    workflows.update([parsedWorkflow])


def partOne():
    for point in points:
        pipeShit(str_to_dict(point))

    total = 0
    for point in result["A"]:
        total += point["x"] + point["m"] + point["a"] + point["s"]

    print(total)


def count(ranges, workflow_name = "in"):
    if (workflow_name in "AR"):
        if (workflow_name == "A"):
            total = 1
            for low, hi in ranges.values():
                total *= hi - low + 1
            return total
        return 0

    total = 0
    workflow = workflows[workflow_name]
    for rule in workflow:
        if ">" in rule:
            category, rest = rule.split(">")
            number, new_workflow_name = rest.split(":")

            valid_range = dict(ranges)
            valid_range[category] = (int(number) + 1, ranges[category][1])
            total += count(valid_range, new_workflow_name)

            ranges = dict(ranges)
            ranges[category] = (ranges[category][0], int(number))
            
        elif "<" in rule:
            category, rest = rule.split("<")
            number, new_workflow_name = rest.split(":")

            valid_range = dict(ranges)
            valid_range[category] = (ranges[category][0], int(number) - 1)
            total += count(valid_range, new_workflow_name)
            
            ranges = dict(ranges)
            ranges[category] = (int(number), ranges[category][1])
        else:
            total += count(ranges, rule)
    
    return total

def partTwo():
    print(count({key: (1,4000) for key in "xmas"}) )
    

# 418498
partOne()
# 123331556462603
partTwo()


