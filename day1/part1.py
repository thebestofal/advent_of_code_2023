output = 0
with open('input.txt') as f:
    for line in f:
        numbers = [i for i in list(line) if i.isdigit()]
        output = output + int(f'{numbers[0] + numbers[-1]}')

print(output)