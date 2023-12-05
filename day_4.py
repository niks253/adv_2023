def get_numbers_set(line: str):
    num_items = line.split(' ')

    nums = set()
    for num_item in num_items:
        str_val = num_item.strip()
        if len(str_val) > 0:
            nums.add(int(str_val))

    return nums


def get_line_amount(line: str):
    line_items = line.split('|')

    winning_line = line_items[0].strip()

    wining_numbers = get_numbers_set(winning_line)

    you_have_line = line_items[1].strip()

    you_have_numbers = get_numbers_set(you_have_line)

    won_numbers = set.intersection(wining_numbers, you_have_numbers)

    return len(won_numbers)


def dfs_card(card_num: int, cards: {}) -> int:
    if cards[card_num] == 0:
        return 1
    else:
        sub_won_cards = 0
        for sub_card_num in get_following_indexes(card_num, cards[card_num]):
            sub_won_cards += dfs_card(sub_card_num, cards)
        return 1 + sub_won_cards

def get_following_indexes(card_num: int, num_won: int):
    indexes = []
    for sub_card_num in range(card_num + 1, card_num + num_won + 1):
        indexes.append(sub_card_num)
    return indexes


def day_4(filename: str):
    total_amount = 0
    cards = {}
    with open(filename, 'r', encoding='UTF-8') as f:
        lines = [line.rstrip('\n') for line in f]
        for line in lines:
            line_items = line.split(': ')
            card_num = int(line_items[0].split(' ')[-1].strip())
            number_of_won = get_line_amount(line_items[1].strip())
            cards[card_num] = number_of_won
            amount = 0
            if number_of_won > 0:
                amount = pow(2,  (number_of_won - 1))
            total_amount += amount

    print(str(total_amount))

    num_cards = 0
    for card_num, number_of_won in cards.items():
        w_a = dfs_card(card_num, cards)
        num_cards += w_a

    print(num_cards)
