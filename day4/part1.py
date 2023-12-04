points = 0

with (open('input.txt') as f):
    for i, line in enumerate(f):
        line = line.split(':')[1]
        winning_numbers = list(int(x) for x in line.split('|')[0].split(' ') if x.isdigit())
        my_numbers = list(int(x) for x in line.replace('\n', '').split('|')[1].split(' ') if x.isdigit())

        count_intersection = 0
        for number in my_numbers:
            if number in winning_numbers:
                count_intersection += 1

        if count_intersection > 0:
            points += 2 ** (count_intersection - 1)

print(points)








