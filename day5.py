from functools import cmp_to_key

input = "day5"

lines = open(input, "r").read().splitlines()

instructions = []
pages_to_print = []

for line in lines:
  if "|" in line:
    instructions.append(list(map(int, line.split("|"))))
  elif "," in line:
    pages_to_print.append(list(map(int, line.split(","))))

def is_in_order(page_to_print):
  for i in range(len(page_to_print)):
    for j in range(i + 1, len(page_to_print)):
      if ([page_to_print[i], page_to_print[j]] not in instructions):
        return False
  return True


def get_middle_value(page_to_print):
  if (is_in_order(page_to_print)):
    return page_to_print[len(page_to_print) // 2]
  
  return 0


def partOne():
  print(sum(get_middle_value(page) for page in pages_to_print))

def partTwo():
  def get_not_valid_order(pages_to_print):
    result = []
    for page_to_print in pages_to_print:
      if (not is_in_order(page_to_print)):
        result.append(page_to_print)

    return result

  def get_middle_point_for_fixed_page(page_to_print: list[int]):
    def compare(left, right):
      if ([left, right] in instructions):
        return -1
      return 1
    
    page_to_print.sort(key=cmp_to_key(compare))

    return get_middle_value(page_to_print)
    
  print(sum(get_middle_point_for_fixed_page(page_to_print) for page_to_print in get_not_valid_order(pages_to_print)))

partOne()
partTwo()
