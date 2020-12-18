data = open('3.txt').read().split('\n')



totals = []
for a, b in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:

    trees = 0

    x = y = 0

    while y < len(data):
        x += a
        y += b
        if y >= len(data):
            break

        if data[y][x%len(data[0])] == '#':
            trees += 1

    totals.append(trees)

from math import prod

print(prod(totals))
