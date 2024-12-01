input = "day1"

location_pairs = open(input, "r").readlines()
left = []
right = []
for locations in location_pairs:
  l,r = locations.split()
  left.append(int(l))
  right.append(int(r))

def partOne():
  left.sort()
  right.sort()

  distance = 0
  for i in range(len(left)):
    distance += abs(right[i] - left[i])

  print(distance)

def partTwo():
  # Array is sorted
  def count_num_in_array(num_to_find, array):
    count = 0
    for i in range(len(array)):
      if array[i] == num_to_find:
        count += 1
      if array[i] > num_to_find:
        break
    return count

  similarity_score = 0
  for i in range(len(left)):
    num_to_find = left[i]
    similarity_score += num_to_find * count_num_in_array(num_to_find, right)
  print(similarity_score)


partOne()
partTwo()