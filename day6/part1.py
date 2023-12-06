import re


def calc_wins(time, record_distance):
    race_wins = 0
    for j in range(1, time):
        if j == 0:
            race_wins += 0
        else:
            distance = j * (time - j)
            if distance >= record_distance:
                race_wins += 1
    return race_wins


with (open('input.txt') as f):
    all_lines = f.readlines()

time = [int(x) for x in re.findall(r'[0-9]+', all_lines[0])]
distance = [int(x) for x in re.findall(r'[0-9]+', all_lines[1])]
output = 1

for i in range(len(time)):
    output *= calc_wins(time[i], distance[i])

print(output)
