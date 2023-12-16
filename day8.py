import ast
import re

lines = open("day8").read().splitlines()

total = sum([len(line) for line in lines])

count = 0
countE = 0
for line in lines:
    countE += len(re.escape(line)) + 4 + (line.count("\"") - 2)
    count += len(ast.literal_eval(line))

print(total - count)
print(countE - total)
