input = 'day9'

disk_map = list(map(int, list(open(input).read())))

def partOne():
  isFile = True
  disk = []
  file_id = 0

  def getEmptySpaceId(disk, start_index):
    for i in range(start_index, len(disk)):
      if disk[i] == '.':
        return i


  for length in disk_map:
    if isFile:
      for a in range(length):
        disk.append(file_id)
      file_id += 1
    else:
      for a in range(length):
        disk.append('.')
    
    isFile = not isFile
  file_id_to_move = len(disk) - 1
  empty_space_id = getEmptySpaceId(disk, 0)

  while empty_space_id < file_id_to_move:
    if disk[file_id_to_move] != '.':
      disk[empty_space_id] = disk[file_id_to_move]
      disk[file_id_to_move] = '.'
      empty_space_id = getEmptySpaceId(disk, empty_space_id)
    file_id_to_move = file_id_to_move - 1

  checksum = 0
  for block_id, block in enumerate(disk):
    if block == '.': break
    checksum += block_id * int(block)

  print(checksum)

def partTwo():

  file_id = 0
  files = {}
  spaces = []
  block_id = 0
  for space_id, length in enumerate(disk_map):
    if (space_id%2 == 0):
      files[file_id] = (file_id, block_id, length)
      file_id += 1
    else:
      if length != 0:
        spaces.append((block_id, length))

    block_id += length

  for file in reversed(files.keys()):
    file_id, block_id, file_length = files[file]
    for space_id, (space_block, space_length) in enumerate(spaces):
      if space_block >= block_id: 
        spaces = spaces[:space_id]
        break
      if space_length >= file_length:
        files[file] = (file_id, space_block, file_length)
        if space_length == file_length:
          spaces.pop(space_id)
        else:
          spaces[space_id] = (space_block + file_length, space_length - file_length)
        break


  f = list(files.values())
  f.sort(key=lambda file: file[1])
  disk = []
  for file_id, file_block, file_length in f:
    if len(disk) != file_block:
      for i in range(file_block - len(disk)):
        disk.append('.')
    for i in range(file_block, file_block + file_length):
      disk.append(file_id)

  checksum = 0
  for block_id, block in enumerate(disk):
    if block == '.': continue
    checksum += block_id * block

  print(checksum)



partOne()
partTwo()

