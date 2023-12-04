from collections import defaultdict


def def_value():
    return 1


qty = defaultdict(def_value)


def intersection(winning_numbers, my_numbers, line):
    count_intersection = 0
    for number in my_numbers:
        if number in winning_numbers:
            count_intersection += 1

    # count how many new cards you won and add it to dict
    for x in range(count_intersection):
        qty[line + x + 1] += qty[line]

    # initialize this value in dict if it is the last one with no match
    if count_intersection == 0:
        qty[line]


with (open('input.txt') as f):
    for i, line in enumerate(f):
        line = line.split(':')[1]
        winning_numbers = list(int(x) for x in line.split('|')[0].split(' ') if x.isdigit())
        my_numbers = list(int(x) for x in line.replace('\n', '').split('|')[1].split(' ') if x.isdigit())
        intersection(winning_numbers, my_numbers, i + 1)

print(sum(list(qty.values())))






