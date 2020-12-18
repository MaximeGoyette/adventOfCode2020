data = open('17.txt').read().split('\n')

coords = {}

for y, line in enumerate(data):
    for x, value in enumerate(line):
        coords[(x, y, 0, 0)] = value

from itertools import product

for _ in range(6):
    new_coords = {}

    to_check = set(coords.keys())

    for x, y, z, w in set(to_check):
        for dx, dy, dz, dw in product(range(-1, 2), repeat=4):
            to_check.add((x + dx, y + dy, z + dz, w + dw))

    for x, y, z, w in to_check:
        active = 0
        v = coords.get((x, y, z, w), '.')

        for dx, dy, dz, dw in product(range(-1, 2), repeat=4):
            if dx == dy == dz == dw == 0:
                continue
            if coords.get((x + dx, y + dy, z + dz, w + dw), '.') == '#':
                active += 1

        if v == '#':
            if active in [2, 3]:
                new_coords[(x, y, z, w)] = '#'
            else:
                new_coords[(x, y, z, w)] = '.'
        elif v == '.':
            if active == 3:
                new_coords[(x, y, z, w)] = '#'
            else:
                new_coords[(x, y, z, w)] = '.'
        else:
            new_coords[(x, y, z, w)] = '.'

    coords = new_coords
    

print([*coords.values()].count('#'))
