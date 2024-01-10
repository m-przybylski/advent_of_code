input = [11, 30, 47, 31, 32, 36, 3, 1, 5, 3, 32, 36, 15, 11, 46, 26, 28, 1, 19, 3]
# input = [20, 15, 10, 5, 5]
total = 150
# total = 25

count = 0
container_perm = []

def fill_container(to_fill: int, containers: list[int], filled_containers: list[int]):
    global count, container_perm
    if to_fill == 0:
        container_perm.append(filled_containers)
        count += 1
        return
    if len(containers) == 0 and to_fill > 0:
        return
    c = containers.copy()
    container = c.pop()
    if container <= to_fill:
        fill_container(to_fill - container, c, [*filled_containers, container])
    
    fill_container(to_fill, c, filled_containers)

fill_container(total, input, [])
min_length = len(min(container_perm, key=lambda x: len(x)))

print(count)
print(len(list(filter(lambda x: len(x) == min_length, container_perm))))
