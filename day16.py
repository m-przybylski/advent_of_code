input = "day16"


def parse_data(line: str):
    def parse_compounds(compound_text: str):
        compound, number = compound_text.split(": ")
        return (compound, int(number))

    aunt, *others = line.replace(":", ",", 1).split(", ")
    _, aunt_number = aunt.split()
    return (int(aunt_number), list(map(parse_compounds, others)))


sues = list(map(parse_data, open(input).read().splitlines()))

result = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

selected_sue = 0
for sue_number, compounds in sues:
    for compound, value in compounds:
        if result[compound] != value:
            break
    else:
        selected_sue = sue_number

print(selected_sue)

for sue_number, compounds in sues:
    for compound, value in compounds:
        if compound in ["cats", "trees"]:
           if result[compound] >= value:
               break
        elif compound in ["pomeranians", "goldfish"]:
            if result[compound] <= value:
               break
        elif result[compound] != value:
            break
    else:
        selected_sue = sue_number

print(selected_sue)

