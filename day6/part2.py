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

time = int(re.findall(r'[0-9]+', all_lines[0].replace(' ', ''))[0])
record_distance = int(re.findall(r'[0-9]+', all_lines[1].replace(' ', ''))[0])

print(calc_wins(time, record_distance))



