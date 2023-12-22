from collections import deque

input = 'input/day22'

def intersectsFromTop(brick1, brick2): 
    return max(brick1[0], brick2[0]) <= min(brick1[3], brick2[3]) and max(brick1[1], brick2[1]) <= min(brick1[4], brick2[4])

def areTouching(upper, lower): 
    return intersectsFromTop(upper, lower) and upper[2] == lower[5] + 1


def partOne():
    bricks = [list(map(int, brick.replace("~", ",").split(","))) for brick in open(input).read().splitlines()]
    bricks.sort(key=lambda brick: brick[2])
    
    for brick_no, brick in enumerate(bricks):
        max_z = 1
        for check in bricks[:brick_no]:
            if intersectsFromTop(brick, check):
                max_z = max(max([check[2],check[5]]) + 1, max_z)
        
        z_diff = abs(brick[5] - brick[2])
        brick[2] = max_z
        brick[5] = max_z + z_diff

    bricks.sort(key=lambda brick: brick[2])

    lower_supporting_upper = {i: set() for i in range(len(bricks))}
    upper_on_top_of_lower = {i: set() for i in range(len(bricks))}

    for upper_index, upper in enumerate(bricks):
        for lower_index, lower in enumerate(bricks[:upper_index]):
            if areTouching(upper, lower):
                lower_supporting_upper[lower_index].add(upper_index)
                upper_on_top_of_lower[upper_index].add(lower_index)

    to_remove = set()
    for brick_index in range(len(bricks)):
        if all([len(upper_on_top_of_lower[upper_index]) >= 2 for upper_index in lower_supporting_upper[brick_index]]):
            to_remove.add(brick_index)

    print(len(to_remove))

def partTwo():
    bricks = [list(map(int, brick.replace("~", ",").split(","))) for brick in open(input).read().splitlines()]
    bricks.sort(key=lambda brick: brick[2])
    
    for brick_no, brick in enumerate(bricks):
        max_z = 1
        for check in bricks[:brick_no]:
            if intersectsFromTop(brick, check):
                max_z = max(max([check[2],check[5]]) + 1, max_z)
        
        z_diff = abs(brick[5] - brick[2])
        brick[2] = max_z
        brick[5] = max_z + z_diff

    bricks.sort(key=lambda brick: brick[2])

    lower_supporting_upper = {i: set() for i in range(len(bricks))}
    upper_on_top_of_lower = {i: set() for i in range(len(bricks))}

    for upper_index, upper in enumerate(bricks):
        for lower_index, lower in enumerate(bricks[:upper_index]):
            if areTouching(upper, lower):
                lower_supporting_upper[lower_index].add(upper_index)
                upper_on_top_of_lower[upper_index].add(lower_index)


    total = 0

    for i in range(len(bricks)):
        q = deque(j for j in lower_supporting_upper[i] if len(upper_on_top_of_lower[j]) == 1)
        falling = set(q)
        falling.add(i)
        
        while q:
            j = q.popleft()
            for k in lower_supporting_upper[j] - falling:
                if upper_on_top_of_lower[k] <= falling:
                    q.append(k)
                    falling.add(k)
        
        total += len(falling) - 1
    print(total)
# 473
partOne()

# 
partTwo()