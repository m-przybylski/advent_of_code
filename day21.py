from collections import deque
from functools import cache
from itertools import product
import re

input = 'day21'

codes = open(input).read().splitlines()
def partOne():
  numpad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [None, '0', 'A']
  ]

  arrows = [
    [None, "^", "A"],
    ["<", "v", ">"]
  ]
  def build_moves(start, end, pad):
    rows = len(pad)
    cols = len(pad[0])
    for r in range(rows):
      for c in range(cols):
        if pad[r][c] == start:
          break
      else:
        continue
      break

    if start == end: return ['A']
    result:list[list] = []
    q = deque()
    q.append(([(r, c, "A")], {(r,c)}))
    while q:
      path, seen = q.pop()
      r,c, _ = path[len(path) - 1]
      for nr, nc, sym in [(r+1,c, "v"), (r-1, c, "^"), (r, c+1, ">"), (r, c-1, "<")]:
        if (nr, nc) in seen: continue
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols: continue
        if pad[nr][nc] == None: continue
        if pad[nr][nc] == end:
          result.append(path[::] + [(nr, nc, sym)])
        else:
          new_seen = seen.copy()
          new_seen.add((nr, nc))
          q.append((path[::] + [(nr, nc, sym)], new_seen))

    a = []
    min_len = float("inf")
    for outcome in result:
      if len(outcome) < min_len:
        a = ["".join(sym for r,c, sym in outcome[1:]) + "A"]
        min_len = len(outcome)
      elif len(outcome) == min_len:
        a.append("".join(sym for r,c, sym in outcome[1:]) + "A")
      else:
        continue

    return a
    

  buttons = ["A", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  robot_a_moves = {}
  for button_from in buttons:
    for button_to in buttons:
      robot_a_moves[(button_from, button_to)] = build_moves(button_from, button_to, numpad)

  arrow_buttons = ["A", "^", ">", "v", "<"]
  robot_b_moves = {}
  for button_from in arrow_buttons:
    for button_to in arrow_buttons:
      robot_b_moves[(button_from, button_to)] = build_moves(button_from, button_to, arrows)

  def getMinLength(array: list):
    smallest = [array[0]]
    
    for i in range(1, len(array)):
      if len(array[i]) < len(smallest[0]):
        smallest = [array[i]]
      elif len(array[i]) == len(smallest[0]):
        smallest.append(array[i])
      else:
        continue
    return smallest


  @cache
  def doMagic(chars):
    result = []
    pos = 'A'
    for arrow in chars:
      moves = robot_b_moves[(pos, arrow)]
      pos = arrow
      if len(result) == 0:
        result = moves
        continue
      result = [(robot_move + move) for robot_move in result for move in moves]
          
    return result


  def enterCode(code: str):
    robots = []

    pos_a = 'A'
    for char in code:
      moves = robot_a_moves[(pos_a, char)]
      pos_a = char
      if len(robots) == 0:
        robots = moves
        continue
      robots = [(robot_a_move + move) for robot_a_move in robots for move in moves]
    
    robots = getMinLength(robots)
    
    for i in range(2):
      new = []
      for robot_b in robots:
        new += doMagic(robot_b)
      robots = getMinLength(new)

    return len(robots[0])

  def getResult(code: str):
    return int("".join(re.findall(r"\d+", code))) * enterCode(code)

  total = 0
  for code in codes:
    total += getResult(code)

  print(total)

partOne()

def partTwo():
  def compute_seqs(keypad):
      pos = {}
      for r in range(len(keypad)):
          for c in range(len(keypad[r])):
              if keypad[r][c] is not None: pos[keypad[r][c]] = (r, c)
      seqs = {}
      for x in pos:
          for y in pos:
              if x == y:
                  seqs[(x, y)] = ["A"]
                  continue
              possibilities = []
              q = deque([(pos[x], "")])
              optimal = float("inf")
              while q:
                  (r, c), moves = q.popleft()
                  for nr, nc, nm in [(r - 1, c, "^"), (r + 1, c, "v"), (r, c - 1, "<"), (r, c + 1, ">")]:
                      if nr < 0 or nc < 0 or nr >= len(keypad) or nc >= len(keypad[0]): continue
                      if keypad[nr][nc] is None: continue
                      if keypad[nr][nc] == y:
                          if optimal < len(moves) + 1: break
                          optimal = len(moves) + 1
                          possibilities.append(moves + nm + "A")
                      else:
                          q.append(((nr, nc), moves + nm))
                  else:
                      continue
                  break
              seqs[(x, y)] = possibilities
      return seqs

  def solve(string, seqs):
      options = [seqs[(x, y)] for x, y in zip("A" + string, string)]
      return ["".join(x) for x in product(*options)]

  num_keypad = [
      ["7", "8", "9"],
      ["4", "5", "6"],
      ["1", "2", "3"],
      [None, "0", "A"]
  ]

  num_seqs = compute_seqs(num_keypad)

  dir_keypad = [
      [None, "^", "A"],
      ["<", "v", ">"]
  ]

  dir_seqs = compute_seqs(dir_keypad)
  dir_lengths = {key: len(value[0]) for key, value in dir_seqs.items()}

  @cache
  def compute_length(seq, depth=25):
      if depth == 1:
          return sum(dir_lengths[(x, y)] for x, y in zip("A" + seq, seq))
      length = 0
      for x, y in zip("A" + seq, seq):
          length += min(compute_length(subseq, depth - 1) for subseq in dir_seqs[(x, y)])
      return length

  total = 0

  for line in open(input).read().splitlines():
      inputs = solve(line, num_seqs)
      length = min(map(compute_length, inputs))
      total += length * int(line[:-1])

  print(total)

partTwo()