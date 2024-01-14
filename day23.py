source = "day23"

instructions = open(source).read().splitlines()

register_a = 0
register_b = 0

def process_instruction(instruction: str, index):
    global register_a, register_b
    
    instr = instruction.split()

    if instr[0] == "hlf":
        if instr[1] == "a":
            register_a /= 2
        if instr[1] == "b":
            register_b /= 2
        return index + 1
    
    if instr[0] == "tpl":
        if instr[1] == "a":
            register_a *= 3
        if instr[1] == "b":
            register_b *= 3
        return index + 1

    if instr[0] == "inc":
        if instr[1] == "a":
            register_a += 1
        if instr[1] == "b":
            register_b += 1
        return index + 1
    
    if instr[0] == "jmp":
        return eval(f"{index}{instr[1]}")
    
    if instr[0] == "jie":
        register_to_check = register_a if instr[1] == "a," else register_b
        should_jump = register_to_check % 2 == 0
        if should_jump:
            return eval(f"{index}{instr[2]}")
        return index + 1

    if instr[0] == "jio":
        register_to_check = register_a if instr[1] == "a," else register_b
        should_jump = register_to_check == 1
        if should_jump:
            return eval(f"{index}{instr[2]}")
        return index + 1

index = 0
while True:
    index = process_instruction(instructions[index], index)
    if index == None or index < 0 or index > len(instructions) - 1:
        break

print(register_a)
print(register_b)

register_a = 1
register_b = 0

index = 0
while True:
    index = process_instruction(instructions[index], index)
    if index == None or index < 0 or index > len(instructions) - 1:
        break

print(register_a)
print(register_b)
