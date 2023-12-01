import re


def translate(test):
    d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    result = []
    for key in d.keys():
        line = list(test)
        if test.find(key) != -1:
            t = [m.start() for m in re.finditer(key, test)]
            for pos in t:
                line[pos] = str(d.get(key))
        result.append(line)

    out = []
    for x in range(len(test) - 1):
        for y in range(len(result)):
            if result[y][x].isdigit():
                out.append(result[y][x])
                break
    return out


output = 0
with open('input.txt') as f:
    for line in f:
        numbers = translate(line)
        output = output + int(f'{numbers[0] + numbers[-1]}')

print(output)