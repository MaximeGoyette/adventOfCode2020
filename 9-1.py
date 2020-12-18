data = open('9.txt').read().split('\n')
data = [int(x) for x in data]

n = 25

from itertools import combinations

for i, line in enumerate(data[n:]):
    valid = False
    for c in combinations(data[i:i+n], 2):
        if sum(c) == line:
            valid = True
    if not valid:
        print(line)
        exit()
