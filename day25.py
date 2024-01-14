row = 2978
column = 3083

# row = 2
# column = 5

diagonal_index = row + column - 1

code = 20151125
multiplier = 252533
divider = 33554393

code_number = sum(range(1, diagonal_index)) + column

for _ in range(1, code_number):
    code = code * multiplier % divider

print(code)