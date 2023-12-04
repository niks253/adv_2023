def process_game_line_2(line: str):
    game_id = line.split(':')[0]
    cube_set_str = line.split(':')[1]
    cube_set_str = cube_set_str.strip()

    cube_lines = cube_set_str.split(';')

    max_colors = {'red': 0, 'green': 0, 'blue': 0}

    for cube_line in cube_lines:
        cube_line = cube_line.strip()
        cube_line_items = cube_line.split(', ')
        for cube_line_item in cube_line_items:
            cube_line_item = cube_line_item.strip()
            sub_item = cube_line_item.split(' ')
            num_cubes = int(sub_item[0])
            cube_color = sub_item[1]
            max_colors[cube_color] = max(max_colors[cube_color], num_cubes)

    return max_colors

# part two
def game_two_2(filename: str):
    sum_of_games = 0
    with open(filename, 'r', encoding='UTF-8') as f:
        lines = [line.rstrip('\n') for line in f]
        for line in lines:
            result = process_game_line_2(line)
            product = result['green'] * result['red'] * result['blue']
            sum_of_games += product

    print('sum ' + str(sum_of_games))


def process_game_line_1(line: str, limits: dict):
    game_id = line.split(':')[0]
    cube_set_str = line.split(':')[1]
    cube_set_str = cube_set_str.strip()

    game_num = int(game_id.split(' ')[1])

    cube_lines = cube_set_str.split(';')

    game_is_valid = True

    stop_cycle = False

    for cube_line in cube_lines:
        cube_line = cube_line.strip()
        if stop_cycle:
            break
        cube_line_items = cube_line.split(', ')
        for cube_line_item in cube_line_items:
            cube_line_item = cube_line_item.strip()
            sub_item = cube_line_item.split(' ')
            num_cubes = int(sub_item[0])
            cube_color = sub_item[1]

            color_limit = limits[cube_color]

            if num_cubes > color_limit:
                game_is_valid = False
                stop_cycle = True
                break

    return {'game_num': game_num, 'is_valid': game_is_valid}

# part one
def game_two_1(filename: str):
    limits = {'red': 12, 'green': 13, 'blue': 14}

    sum_of_games = 0
    with open(filename, 'r', encoding='UTF-8') as f:
        lines = [line.rstrip('\n') for line in f]
        for line in lines:
            result = process_game_line_1(line, limits)
            if result['is_valid']:
                sum_of_games += result['game_num']

    print('sum ' + str(sum_of_games))
