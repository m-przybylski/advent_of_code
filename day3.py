input = "day3"

bank = list(list(line.strip()) for line in open(input, "r").readlines())

def part_one():
  total_joltage = 0
  for battery in bank:
    max_joltage = max(battery)
    index = battery.index(max_joltage)
    if index == len(battery) -1:
      second_max_joltage = max(battery[:-1])
      total_joltage += int(second_max_joltage + max_joltage)
    else:
      second_max_joltage = max(battery[index+1:])
      total_joltage += int(max_joltage + second_max_joltage)

  print(total_joltage)

def part_two():
  total_joltage = 0
  batteries_to_turn_on = 12
  for battery in bank:
    battery_joltage = ''
    max_joltage = max(battery[:-batteries_to_turn_on])
    index = battery.index(max_joltage)
    battery_joltage = max_joltage
    remaining_battery = battery[index+1:]
    # check if we can drop any batteries
    while len(battery_joltage) + len(remaining_battery) > batteries_to_turn_on:
      max_joltage = max(remaining_battery[:-batteries_to_turn_on+len(battery_joltage)+1 or None])
      index = remaining_battery.index(max_joltage)
      battery_joltage += max_joltage
      remaining_battery = remaining_battery[index+1:] if len(battery_joltage) < batteries_to_turn_on else []
    battery_joltage = battery_joltage + "".join(remaining_battery)
    total_joltage += int(battery_joltage)

  print(total_joltage)
  

part_one()
part_two()
