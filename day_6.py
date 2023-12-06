def parse_line(line: str) -> []:
    nums_str = line.split(':')[1]

    num_str_items = nums_str.split(' ')

    nums = []

    for num_str in num_str_items:
        nn = num_str.strip()
        if len(nn) > 0:
            num = int(nn)
            nums.append(num)
    return nums


def get_distance(speed: int, time: int) -> int:
    return speed * time


def get_num_ways(race_time: int, record_distance: int) -> int:
    num_ways = 0

    for hold_time in range(0, race_time):
        dist = get_distance(hold_time, race_time - hold_time)

        if dist > record_distance:
            num_ways += 1

    return num_ways


def day_6(filename: str) -> None:
    times = []
    distances = []

    with open(filename, 'r', encoding='UTF-8') as f:
        lines = [line.rstrip('\n') for line in f]

        for line in lines:
            if line.startswith('Time:'):
                times = parse_line(line)
            elif line.startswith('Distance:'):
                distances = parse_line(line)


    print(times)
    print(distances)

    mult = 1
    for i in range(0, len(times)):
        num_ways = get_num_ways(times[i], distances[i])
        mult *= num_ways

    print(mult)

    race_time = int(''.join(map(str, times)))
    record_distance = int(''.join(map(str, distances)))

    num_ways = get_num_ways(race_time, record_distance)
    print(num_ways)

if __name__ == '__main__':
    day_6("input_day_6_2.txt")
