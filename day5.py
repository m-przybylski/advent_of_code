input = 'day5'

database = list(row.strip() for row in open(input, 'r').readlines())

fresh_ingredient_IDs = []
available_products = []
for row in database:
  if row == "":
    continue
  if "-" in row:
    fresh_ingredient_IDs.append(tuple(map(int, row.split("-"))))
  else:
    available_products.append(int(row))

fresh_ingredient_IDs.sort()

def part_one():
  count = 0
  for available_product in available_products:
    for (start, end) in fresh_ingredient_IDs:
      if start <= available_product and available_product <= end:
        count += 1
        break

  print(count)

def part_two():
  count = 0
  last_processed_ingredient_range = None
  for start, end in fresh_ingredient_IDs:
    if (last_processed_ingredient_range is None): 
      last_processed_ingredient_range = (start, end)
    elif last_processed_ingredient_range[1] < start:
      count += last_processed_ingredient_range[1] - last_processed_ingredient_range[0] + 1
      last_processed_ingredient_range = (start, end)
    else:
      last_processed_ingredient_range = (last_processed_ingredient_range[0], max(last_processed_ingredient_range[1], end))
  
  count += last_processed_ingredient_range[1] - last_processed_ingredient_range[0] + 1
  
  print(count)

part_one()
part_two()