count = 1
puzzle_input = 33100000

import math

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

house = 0
while True:
    house += 1
    if sum(divisorGenerator(house)) * 10 >= puzzle_input:
        break

# 776160
print(house)

limit = 1_000_000
houses = dict.fromkeys(range(1, limit + 1), 0)
for elf in range(1, limit):
    top = min(elf * 50 + 1, limit)
    for j in range(elf, top, elf):
        houses[j] += elf * 11
        if houses[j] >= puzzle_input:
            limit = j
            break

for house, presents in houses.items():
    if presents >= puzzle_input:
        print(house)
        break