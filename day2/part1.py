import re

output = 0
all_games = 0
bag = {'red': 12, 'green': 13, 'blue': 14}
with open('input.txt') as f:
    for i, line in enumerate(f, start=1):
        line = line[line.find(':') + 1:]
        arr_line = line.split(';')
        for set in arr_line:
            for pair in set.split(','):
                number = re.sub(r'[^0-9\s]', '', pair)
                color = re.sub(r'[0-9\s]', '', pair)

                if bag[color] < int(number):
                    break
            else:
                continue
            output += i
            break
        all_games += i

print(all_games - output)
