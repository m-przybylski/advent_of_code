input = "day7"

instructions = open(input, 'r').read().splitlines()
resolved = {}

def toUInt16(value):
    if value < 0:
        value += 65536
    if value > 65535:
        value -= 65536
    return value

# def getValueAt(wire: str):
#     global instructions, resolved

#     if (wire in resolved):
#         return resolved[wire]


    
#     if (wire.isdigit()):
#         return int(wire)

#     for instruction in instructions:
#         left, right = instruction.split(" -> ")
#         if right == wire:
#             ops = left.split()
            
#             if left.isdigit():
#                 resolved[wire] = int(left)
#                 return int(left)
            
#             if len(ops) == 1:
#                 print(ops[0])
#                 return getValueAt(ops[0])
            
#             if "AND" in left:
#                 return getValueAt(ops[0]) & getValueAt(ops[2])
            
#             if "OR" in left:
#                 return getValueAt(ops[0]) | getValueAt(ops[2])
            
#             if "RSHIFT" in left:
#                 return toUInt16(getValueAt(ops[0]) >> int(ops[2]))

#             if "LSHIFT" in left:
#                 return toUInt16(getValueAt(ops[0]) << int(ops[2]))

#             if "NOT" in left:
#                 return toUInt16(~getValueAt(ops[1]))

#         else:
#             continue
        
#         raise RuntimeError("This should not happen", wire)

def solveCircuit(instructions: list, wireToSolve: str) -> int:
    wires = {}
    def getWireValueOrWireName(wire: str) -> int | str:
        if wire.isdigit():
            return int(wire)
        if wire in wires:
            return wires[wire]
        return wire

    while True:
        if wireToSolve in wires:
            return wires[wireToSolve]

        for instruction in instructions:
            ops = instruction.split()

            if len(ops) == 3:
                # a -> b
                if ops[0].isdigit():
                    wires[ops[2]] = int(ops[0])
                elif ops[0] in wires:
                    wires[ops[2]] = wires[ops[0]]

                continue

            if len(ops) == 4:
                # NOT a -> b
                if ops[1].isdigit(): 
                    wires[ops[3]] = toUInt16(~ops[1])

                if ops[1] in wires:
                    wires[ops[3]] = toUInt16(~wires[ops[1]])

                continue
            
            # a AND b -> 3
            if ops[1] == "AND":
                left = getWireValueOrWireName(ops[0])
                right = getWireValueOrWireName(ops[2])

                if isinstance(left, int) and isinstance(right, int):
                    wires[ops[4]] = toUInt16(left & right)
                
                continue
                
            # a OR b -> 3
            if ops[1] == "OR":
                left = getWireValueOrWireName(ops[0])
                right = getWireValueOrWireName(ops[2])

                if isinstance(left, int) and isinstance(right, int):
                    wires[ops[4]] = toUInt16(left | right)
                
                continue

            # a RSHIFT b -> 3
            if ops[1] == "RSHIFT":
                left = getWireValueOrWireName(ops[0])
                shift = int(ops[2])

                if isinstance(left, int):
                    wires[ops[4]] = toUInt16(left >> shift)
            
                continue

            # a LSHIFT b -> 3
            if ops[1] == "LSHIFT":
                left = getWireValueOrWireName(ops[0])
                shift = int(ops[2])

                if isinstance(left, int):
                    wires[ops[4]] = toUInt16(left << shift)
                
                continue



def partOne():
    result = solveCircuit(instructions, "a")
    print(result)

def partTwo():
    result = solveCircuit(instructions, "a")
    for idx, instruction in enumerate(instructions):
        if instruction.endswith("-> b"):
            del instructions[idx]
            break

    instructions.append(str(result) + " -> b")
    result = solveCircuit(instructions, "a")
    print(result)
    
# 956
partOne()

# 40149
partTwo()