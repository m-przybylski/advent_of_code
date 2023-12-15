input = "day1"

map = open(input, "r").read()

up = 0
down = 0

for ch in map:
    if ch == "(":
        up +=1
    elif ch == ")":
        down += 1

print(up - down)


level = 0
count = 0
for ch in map:
    count +=1
    if ch == "(":
        level += 1
    else:
        level -= 1

    if level == -1:
        break

print(count)