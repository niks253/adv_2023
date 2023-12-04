def get_adj_chars(chart: [[]], c: int, r: int, moves):
    adj_chars = []
    for move in moves:
        n_pos_x = move[0] + c
        n_pos_y = move[1] + r

        if n_pos_x < 0 or n_pos_x >= len(chart[0]):
            continue
        if n_pos_y < 0 or n_pos_y >= len(chart):
            continue

        adj_ch = chart[n_pos_y][n_pos_x]
        adj_chars.append(adj_ch)

    return adj_chars

def get_adj_stars_with_coord(chart: [[]], c: int, r: int, moves):
    adj_chars = []
    for move in moves:
        n_pos_x = move[0] + c
        n_pos_y = move[1] + r

        if n_pos_x < 0 or n_pos_x >= len(chart[0]):
            continue
        if n_pos_y < 0 or n_pos_y >= len(chart):
            continue

        adj_ch = chart[n_pos_y][n_pos_x]
        if adj_ch == '*':
            adj_chars.append({'char': adj_ch, 'x': n_pos_x, 'y': n_pos_y})

    return adj_chars

def adj_chars_has_symbol(adj_chars):
    for adj_ch in adj_chars:
        if not adj_ch == '.':
            return True
    return False


def find_adj_symbols(chart: [[]]):
    left_moves = [[-1, 0], [-1, 1], [0, 1], [1, 1], [0, -1], [-1, -1], [-1, 1]]
    middle_moves = [[0, -1], [-1, -1], [1, -1], [0, 1], [1, 1], [-1, 1]]
    right_moves = [[0, 1], [1, 1], [1, 0], [-1, 1], [1, -1], [0, -1], [-1, -1]]

    sum1 = 0

    star_coord_to_num = {}

    for r, line in enumerate(chart, 0):
        c = 0
        while c < len(line):
            ch = line[c]

            if not ch.isdigit():
                c += 1
                continue
            else:
                num_right_c, num_str = get_number(line, c)

                adj_starts_with_ccords = get_adj_stars_with_coord(chart=chart, c=c, r=r, moves=left_moves)
                adj_starts_with_ccords.extend(
                    get_adj_stars_with_coord(chart=chart, c=num_right_c, r=r, moves=right_moves)
                )

                adj_chars_left = get_adj_chars(chart=chart, c=c, r=r, moves=left_moves)
                adj_chars_right = get_adj_chars(chart=chart, c=num_right_c, r=r, moves=right_moves)

                num_cc = c + 1
                adj_chars_middle = []
                while num_cc < num_right_c:
                    dd = get_adj_chars(chart=chart, c=num_right_c, r=r, moves=middle_moves)
                    adj_chars_middle.extend(dd)

                    adj_starts_with_ccords.extend(
                        get_adj_stars_with_coord(chart=chart, c=num_right_c, r=r, moves=middle_moves)
                    )

                    num_cc += 1

                # a bit of overlapping. do not have time to investigate the details
                dedup_dict = {}
                for adj_star_with_ccords in adj_starts_with_ccords:
                    key = adj_star_with_ccords['y'] * len(line) + adj_star_with_ccords['x']
                    nn_str = ''.join(num_str)
                    dedup_dict[key] = int(nn_str)

                for kk, dedup_item in dedup_dict.items():
                    star_coord_to_num.setdefault(kk, []).append(dedup_item)

                if adj_chars_has_symbol(adj_chars_left) \
                    or adj_chars_has_symbol(adj_chars_right) \
                        or adj_chars_has_symbol(adj_chars_middle):
                    nn_str = ''.join(num_str)
                    sum1 += int(nn_str)

                c = num_right_c + 1
    print(sum1)

    sum2 = 0

    for key, item in star_coord_to_num.items():
        if len(item) == 2:
            sum2 += item[0] * item[1]
    
    print(sum2)


def get_number(line, c):
    num_left_c = c - 1
    while num_left_c >= 0 and line[num_left_c].isdigit():
        num_left_c -= 1
    num_left_c += 1

    num_right_c = c + 1
    while num_right_c < len(line) and line[num_right_c].isdigit():
        num_right_c += 1
    num_right_c -= 1

    num_str = line[num_left_c:num_right_c+1]
    return num_right_c,num_str


def day_3(filename: str):
    chart = []
    with open(filename, 'r', encoding='UTF-8') as f:
        lines = [line.rstrip('\n') for line in f]
        for line_index, line in enumerate(lines, 0):
            ch_list = []
            for ch_index, ch in enumerate(line, 0):
                ch_list.append(ch)
            chart.append(ch_list)
    find_adj_symbols(chart)
