input = "day13"

def read_rule(rule: str) -> (str, str, int):
    rule = rule.replace(".", "")
    words = rule.split()
    who = words[0]
    next_to_who = words[-1]
    value = int(words[3]) * (-1 if words[2] == "lose" else 1)

    return (who, next_to_who, value)

def quick_perm(names: list[str]):
    outcome = []
    length = len(names)
    a = list(range(length))
    p = list(range(length + 1))
    i = 0

    while (i < length):
        p[i] -= 1
        j = i % 2 * p[i]
        tmp = a[j]
        a[j] = a[i]
        a[i] = tmp
        outcome.append([names[index] for index in a])
        i = 1
        while (p[i] == 0):
            p[i] = i
            i += 1

    return outcome

def get_happiness_for_sitting(sitting: list[str], happiness: dict):
    happiness_score = 0
    for index, name in enumerate(sitting):
        next_index = 0 if index + 1 >= len(sitting) else index + 1
        next = sitting[next_index]
        prev = sitting[index - 1]
        happiness_score += happiness[name][next]
        happiness_score += happiness[name][prev]
    return happiness_score

rules = list(map(read_rule, open(input).read().splitlines()))

happiness = {}

for who, next_to, value in rules:
    if who not in happiness:
        happiness[who] = {}
    happiness[who][next_to] = value

sittings = quick_perm(list(happiness.keys()))

max_happiness = -100000000000000
perfect_sitting = []
for sitting in sittings:
    happiness_score = get_happiness_for_sitting(sitting, happiness)

    if max_happiness < happiness_score:
        max_happiness = happiness_score
        perfect_sitting = sitting
    
print(max_happiness)
print(perfect_sitting)

happiness["me"] = {}
for name in happiness:
    happiness[name]["me"] = 0
    happiness["me"][name] = 0

max_happiness = -1000000000
for i in range(len(perfect_sitting)):
    new_sitting = perfect_sitting[:]
    new_sitting.insert(i, "me")
    happiness_score = get_happiness_for_sitting(new_sitting, happiness)
    if max_happiness < happiness_score:
        max_happiness = happiness_score

print(max_happiness)