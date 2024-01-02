input = "day1"

floor_map = open(input, "r").read()

print(floor_map.count("(") - floor_map.count(")"))

level = 0
count = 0
for ch in floor_map:
    count +=1
    if ch == "(":
        level += 1
    else:
        level -= 1

    if level == -1:
        break

print(count)