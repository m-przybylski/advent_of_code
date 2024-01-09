input = "day14"

def parse_data(line: str) -> (str, int, int, int):
    words = line.split()
    return (words[0], int(words[3]), int(words[6]), int(words[-2]))

def get_distance_at(seconds: int, reindeers):
    max_distance = 0
    winner = None
    for name, speed, time_running, time_standing in reindeers:
        distance_in_cycle = speed * time_running
        cycle_duration = time_running + time_standing
        total_cycles = int(seconds / cycle_duration)
        distance = total_cycles * distance_in_cycle
        time_left = seconds if total_cycles == 0 else seconds % cycle_duration
        distance += distance_in_cycle if time_left >= time_running else time_left * speed

        if max_distance < distance:
            max_distance = distance
            winner = name

    return (max_distance, winner)



reindeer_speed = list(map(parse_data, open(input).read().splitlines()))

time = 2503

print(get_distance_at(time, reindeer_speed)[0])

scores = {}

for name, *_ in reindeer_speed:
    scores[name] = 0

for i in range(1, time + 1):
    distance, winner = (get_distance_at(i, reindeer_speed))
    scores[winner] += 1

print(scores[max(scores, key=scores.get)])
