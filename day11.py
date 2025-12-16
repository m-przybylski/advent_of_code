import sys
from collections import defaultdict

# Read all lines from stdin
graph = defaultdict(list)
for line in sys.stdin:
    parts = line.strip().split()
    if not parts:
        continue
    device = parts[0][:-1]
    outputs = parts[1:]
    graph[device].extend(outputs)


def part_one():
    count = 0
    print(graph)
    def dfs(current, visited):
        nonlocal count
        if current == "out":
            count += 1
            return
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                new_visited = visited.copy()
                new_visited.add(neighbor)
                dfs(neighbor, new_visited)

    # Start DFS from 'you' with itself marked as visited
    if "you" in graph:
        dfs("you", {"you"})

    print(count)

def part_two():
  from functools import cache

  @cache
  def count(src, dst):
      if src == dst: return 1
      return sum(count(x, dst) for x in graph.get(src, []))

  print(
      count("svr", "dac") * count("dac", "fft") * count("fft", "out") \
    + count("svr", "fft") * count("fft", "dac") * count("dac", "out")
  )
if __name__ == "__main__":
    part_one()
    part_two()