import requests
import os


day = input("Enter day for which you need an input: ")

re = requests.get(f'https://adventofcode.com/2023/day/{day}/input', cookies={'session': os.getenv('AOC_SESSION')})

if not os.path.exists(f'day{day}/input.txt'):
    os.makedirs(f'day{day}')

with open(f'day{day}/input.txt', 'w') as f:
    f.write(re.text)
