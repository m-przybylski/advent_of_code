import itertools

input = open('day17').read()

def partOne():
  registers, program = input.split("\n\n")
  register = []
  for r in registers.splitlines():
    register.append(int(r.split(": ")[1]))

  program = list(map(int, program.split(": ")[1].split(",")))
  a,b,c = register
  pointer = 0
  out = []
  while pointer < len(program):
      ins = program[pointer]
      operand = program[pointer + 1]
      if ins == 0: # adv
          a = a >> 3
      elif ins == 1: # bxl
          b = b ^ operand
      elif ins == 2: # bst
          b = a % 8
      elif ins == 3: # jnz
          if a != 0:
              pointer = operand
              continue
      elif ins == 4: # bxc
          b = b ^ c
      elif ins == 5: # out
          out.append(b % 8)
      elif ins == 7: # cdv
          c = a >> b
      pointer += 2

  print(*out, sep=",") 

def partTwo():
  _, program = input.split("\n\n")
  program = list(map(int, program.split(": ")[1].split(",")))

  def find(target, ans):
    if target == []: return ans
    for t in range(8):
        a = ans << 3 | t
        b = 0
        c = 0
        output = None
        adv3 = False

        def combo(operand):
            if 0 <= operand <= 3: return operand
            if operand == 4: return a
            if operand == 5: return b
            if operand == 6: return c
            raise AssertionError(f"unrecognized combo operand {operand}")

        for pointer in range(0, len(program) - 2, 2):
            ins = program[pointer]
            operand = program[pointer + 1]
            if ins == 0:
                assert not adv3, "program has multiple ADVs"
                assert operand == 3, "program has ADV with operand other than 3"
                adv3 = True
            elif ins == 1:
                b = b ^ operand
            elif ins == 2:
                b = combo(operand) % 8
            elif ins == 3:
                raise AssertionError("program has JNZ inside expected loop body")
            elif ins == 4:
                b = b ^ c
            elif ins == 5:
                assert output is None, "program has multiple OUT"
                output = combo(operand) % 8
            elif ins == 6:
                b = a >> combo(operand)
            elif ins == 7:
                c = a >> combo(operand)
            if output == target[-1]:
                if a == 0: continue
                sub = find(target[:-1], a)
                if sub is None: continue
                return sub

  print(find(program, 0))
  

partOne()
partTwo()
