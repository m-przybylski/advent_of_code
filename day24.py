from functools import reduce
from itertools import combinations

present_weights = list(map(int, open("day24").read().splitlines()))

total = sum(present_weights) // 3

ARBITRARY_HIGH_VALUE = 999999999999999
min_quantum_entanglement = ARBITRARY_HIGH_VALUE


for no_packages in range(2, len(present_weights)):
    for arrangement in combinations(present_weights, no_packages):
        if sum(arrangement) == total:
            min_quantum_entanglement = min(
                min_quantum_entanglement,
                reduce(lambda x, y: x * y, arrangement))

    if min_quantum_entanglement < ARBITRARY_HIGH_VALUE:
        break

print(min_quantum_entanglement)

total = sum(present_weights) // 4

min_quantum_entanglement = ARBITRARY_HIGH_VALUE


for no_packages in range(2, len(present_weights)):
    for arrangement in combinations(present_weights, no_packages):
        if sum(arrangement) == total:
            min_quantum_entanglement = min(
                min_quantum_entanglement,
                reduce(lambda x, y: x * y, arrangement))

    if min_quantum_entanglement < ARBITRARY_HIGH_VALUE:
        break

print(min_quantum_entanglement)
