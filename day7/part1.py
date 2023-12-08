from collections import Counter


def hand_to_value(hand):
    match sorted(Counter(hand).values()):
        case [5]: # five of a kind
            return 7
        case [1, 4]: # four of a kind
            return 6
        case [2, 3]: # Full house
            return 5
        case [1, 1, 3]: # three of a kind
            return 4
        case [1, 2, 2]: # two pair
            return 3
        case [1, 1, 1, 2]: # one pair
            return 2
        case [1, 1, 1, 1, 1]: # high card
            return 1
        case _:
            return ValueError


def tie(hand, card_values):
    return tuple(card_values.index(c) for c in hand)


cardvalues = '23456789TJQKA'
rank_hands = []

with (open('input.txt') as f):
    for line in f:
        hand, bid = line.split()
        rank_hands.append((hand_to_value(hand), tie(hand, cardvalues), int(bid)))


sum = 0
for i, hand in enumerate(sorted(rank_hands)):
    sum += (i + 1) * hand[2]

print(sum)






