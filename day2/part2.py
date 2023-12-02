import re
import numpy as np

output = 0
with open('input.txt') as f:
    for line in f:
        min_bag = {}
        line = line[line.find(':') + 1:]
        arr_line = line.split(';')
        for set in arr_line:
            for pair in set.split(','):
                number = re.sub(r'[^0-9\s]', '', pair)
                color = re.sub(r'[0-9\s]', '', pair)

                try:
                    if min_bag[color] < int(number):
                        min_bag[color] = int(number)
                except:
                    min_bag[color] = int(number)

        power = np.prod(list(min_bag.values()))
        output += power

print(output)
