input = "day19"

transformations, molecule = open(input).read().split("\n\n")

result = set()

for transformation in transformations.splitlines():
    from_molecule, to_molecule = transformation.split(" => ")
    molecule.count(from_molecule)
    index = 0
    while True:
        try:
            exists = molecule.index(from_molecule, index)
            new_molecule = molecule[:exists] + to_molecule + molecule[exists + len(from_molecule):]
            result.add(new_molecule)
            index = exists + 1
        except:
            break


print(len(result))


m = molecule
count = 0
while True:
    done = True
    for transformation in transformations.splitlines():
        from_molecule, to_molecule = transformation.split(" => ")
        if m.count(to_molecule) > 0:
            index = m.index(to_molecule)
            m = m[:index] + from_molecule + m[index + len(to_molecule):]
            count += 1
            done = False


    if done:
        break

print(m, count)
