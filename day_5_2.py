import sys

def parse_seeds(line: str) -> []:
    seed_str = line.split(':')[1]
    seed_items = seed_str.split(' ')

    seeds = []
    for seed_item in seed_items:
        seed_item = seed_item.strip()
        if len(seed_item) > 0:
            seeds.append(int(seed_item))

    return seeds


def parse_map_line(line: str) -> []:
    map_items = line.split(' ')

    map = []
    for map_item in map_items:
        map.append(int(map_item))

    return map


def parse_map_name(line: str) -> {}:
    name_items = line.split(' ')
    dst_src_list = name_items[0].split('-to-')

    return {'dst': dst_src_list[1], 'src': dst_src_list[0]}


def find_source_map(src: str, maps: []) -> {}:
    for map in maps:
        if map['name']['src'] == src:
            return map
    return None

    
def range_overlapping(x: [], y: []):
    return x[0] <= y[1] and y[0] <= x[1]


def overlap(x: [], y: []):
    if not range_overlapping(x, y):
        return []
    return [max(x[0], y[0]), min(x[1], y[1])]


def map_src_range_to_dst(src_range: [], map: {}) -> []:
    lines = map['lines']

    src_range_to_check = src_range.copy()

    gap_intervals = []

    dst_intervals = []

    any_overlap = False

    for interval_line in lines:
        src_interval = [interval_line[1], interval_line[1] + interval_line[2]]
        dst_interval = [interval_line[0], interval_line[0] + interval_line[2]]

        overlap_interval = overlap(src_range_to_check, src_interval)

        if len(overlap_interval) > 0:
            any_overlap = True
            delta = overlap_interval[0] - src_interval[0]
            #if delta == 0:
            #    print(delta)
            overlap_size = overlap_interval[1] - overlap_interval[0]

            dst_overlap_interval = [dst_interval[0] + delta, dst_interval[0] + delta + overlap_size]

            dst_intervals.append(dst_overlap_interval)

            if src_range_to_check[0] < overlap_interval[0]:
                gap_interval = [src_range_to_check[0], overlap_interval[0]]
                gap_intervals.append(gap_interval)
    
            if src_range_to_check[1] > overlap_interval[1]:
                interval_to_check = [overlap_interval[1], src_range_to_check[1]]
                src_range_to_check = interval_to_check.copy()

    if not any_overlap:
        gap_intervals.append(src_range)

    for gap_interval in gap_intervals:
        dst_intervals.append(gap_interval)

    return dst_intervals

def seed_range_to_location(seed_range_p: [], maps: []) -> []:
    source = 'seed'
    destination = 'location'

    seed_ranges = [seed_range_p]

    while True:
        src_to_dst_map = find_source_map(source, maps)

        if src_to_dst_map == None:
            break

        dst_seed_ranges = []

        for seed_range in seed_ranges:
            dst_seed_ranges.extend(map_src_range_to_dst(seed_range, src_to_dst_map))

        seed_ranges = dst_seed_ranges.copy()

        if src_to_dst_map['name']['dst'] == destination:
            return dst_seed_ranges
        else:
            source = src_to_dst_map['name']['dst']

    return []
    
def day_5(filename: str) -> None:
    seeds = []
    maps = []

    with open(filename, 'r', encoding='UTF-8') as f:
        lines = [line.rstrip('\n') for line in f]

        current_map = {}

        for line in lines:
            if line.startswith('seeds:'):
                seeds = parse_seeds(line)
            elif '-to-' in line:
                map_name = parse_map_name(line)
                current_map['name'] = map_name
            elif len(line) == 0:
                if len(current_map.keys()) > 0:
                    maps.append(current_map.copy())
                current_map.clear()
            else:
                map_line = parse_map_line(line)
                current_map.setdefault('lines', []).append(map_line)
                
        if len(current_map.keys()) > 0:
            maps.append(current_map.copy())
        current_map.clear()
 
    for map in maps:
        map['lines'].sort(key = lambda x: x[1])

    min1 = sys.maxsize

    source_ranges = []

    for i in range(0, int(len(seeds) / 2)):
        start_seed = seeds[i * 2]
        seed_range = seeds[i * 2 + 1]

        source_ranges.append([start_seed, start_seed + seed_range])

    source_ranges.sort(key = lambda x: x[0])

    current_interval = source_ranges[0].copy()
    normalized_ranges = []

    interval_i = 1

    while interval_i < len(source_ranges):
        if source_ranges[interval_i][0] <= current_interval[1]:
            current_interval[1] = source_ranges[interval_i][1]
        else:
            normalized_ranges.append(current_interval)
            current_interval = source_ranges[interval_i].copy()

        interval_i += 1

    if len(current_interval) > 0:
        normalized_ranges.append(current_interval)

    for n_range in normalized_ranges:
        locations = seed_range_to_location(n_range, maps)
        for location in locations:
            min1 = min(min1, location[0])

    print(min1)
 
    # part one removed code. can use single point ranges for part one
    #  for n_range in normalized_ranges:
    #     for seed in range(n_range[0], n_range[1]):
    #         location = seed_to_location(seed, maps)
    #         min1 = min(min1, location)

if __name__ == '__main__':
    day_5("input_day_5.txt")
