from functools import cmp_to_key

def parse_line(line: str) -> {}:
    items = line.split(' ')
    pair = {'hand': items[0].strip(), 'bid': int(items[1].strip())}
    return pair

card_strength = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}

def resolve_tie(hand1: str, hand2: str) -> int:
    for i in range(len(hand1)):
        ch1 = hand1[i]
        ch2 = hand2[i]
        st1 = card_strength[ch1]
        st2 = card_strength[ch2]

        if st1 != st2:
            if st1 > st2:
                return 1
            else:
                return 2
    
    return None

def get_type(hand: str) -> int:
    freq = {}
    for ch in hand:
        freq.setdefault(ch, 0)
        freq[ch] += 1

    amounts = {}
    for key, value in freq.items():
        amounts.setdefault(value, 0)
        amounts[value] += 1

    if len(amounts) == 1 and 5 in amounts:
        return 7
    
    if len(amounts) == 2:
        if 4 in amounts:
            return 6
        if 3 in amounts and 2 in amounts:
            return 5
        if 3 in amounts and 1 in amounts:
            return 4
        if 2 in amounts and amounts[2] == 2:
            return 3
        if 2 in amounts and amounts[1] == 3:
            return 2
        
    if len(amounts) == 1 and 1 in amounts:
        return 1
    
    return None

def compare_hands(pair1: {}, pair2: {}) -> int:
    type1 = get_type(pair1['hand'])
    type2 = get_type(pair2['hand'])

    if type1 > type2:
        return 1
    elif type2 > type1:
        return -1
     
    tie = resolve_tie(pair1['hand'], pair2['hand'])
    if tie == 1:
        return 1
    elif tie == 2:
        return -1
    
    return 0

def total_winnings(pairs: []) -> int:
    pairs.sort(key=cmp_to_key(compare_hands))

    sum = 0
    rank = 1
    for pair in pairs:
        sum += pair['bid'] * rank
        rank += 1

    return sum

def day_7(filename: str) -> None:
    pairs = []

    with open(filename, 'r', encoding='UTF-8') as f:
        lines = [line.rstrip('\n') for line in f]
        for line in lines:
            pair = parse_line(line)
            pairs.append(pair)

    print(pairs)
    get_type(pairs[0]['hand'])
    winnings = total_winnings(pairs)

    print(winnings)

if __name__ == '__main__':
    day_7("input_7_2.txt")
