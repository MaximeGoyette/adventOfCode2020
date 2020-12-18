data = open('17.txt').read().split('\n')

coords = {}

for y, line in enumerate(data):
    for x, value in enumerate(line):
        coords[(x, y, 0)] = value

from itertools import product

for _ in range(6):
    new_coords = {}

    to_check = set(coords.keys())

    for x, y, z in set(to_check):
        for dx, dy, dz in product(range(-1, 2), repeat=3):
            to_check.add((x + dx, y + dy, z + dz))

    for x, y, z in to_check:
        active = 0
        v = coords.get((x, y, z), '.')

        for dx, dy, dz in product(range(-1, 2), repeat=3):
            if dx == dy == dz == 0:
                continue
            if coords.get((x + dx, y + dy, z + dz), '.') == '#':
                active += 1

        if v == '#':
            if active in [2, 3]:
                new_coords[(x, y, z)] = '#'
            else:
                new_coords[(x, y, z)] = '.'
        elif v == '.':
            if active == 3:
                new_coords[(x, y, z)] = '#'
            else:
                new_coords[(x, y, z)] = '.'
        else:
            new_coords[(x, y, z)] = '.'

    coords = new_coords
    

print([*coords.values()].count('#'))
