from copy import deepcopy
from functools import lru_cache

data = [list(x) for x in open('11.txt').read().split('\n')]

adjacents = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

@lru_cache(None)
def find_adjacents(x, y):
    found = set()
    for dx, dy in adjacents:
        nx, ny = x + dx, y + dy
        while True:
            if nx < 0 or nx >= len(data[0]) or ny < 0 or ny >= len(data):
                break
            elif data[ny][nx] in '#L':
                found.add((nx, ny))
                break
            nx += dx
            ny += dy
    return found

while True:
    new_data = deepcopy(data)

    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == 'L' and all(data[dy][dx] in 'L.' for dx, dy in find_adjacents(x, y)):
                new_data[y][x] = '#'
            elif data[y][x] == '#' and len([1 for dx, dy in find_adjacents(x, y) if data[dy][dx] == '#']) >= 5:
                new_data[y][x] = 'L'

    if data == new_data:
        print(''.join(''.join(x) for x in new_data).count('#'))
        exit()

    data = new_data
