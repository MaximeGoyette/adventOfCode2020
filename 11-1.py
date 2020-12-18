from copy import deepcopy

data = [list(x) for x in open('11.txt').read().split('\n')]

adjacents = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

while True:
    new_data = deepcopy(data)

    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == 'L' and all(data[y + dy][x + dx] in 'L.' for dx, dy in adjacents if 0 <= y + dy < len(data) and 0 <= x + dx < len(data[0])):
                new_data[y][x] = '#'
            elif data[y][x] == '#' and len([1 for dx, dy in adjacents if 0 <= y + dy < len(data) and 0 <= x + dx < len(data[0]) and data[y + dy][x + dx] == '#']) >= 4:
                new_data[y][x] = 'L'

    if data == new_data:
        print(''.join(''.join(x) for x in new_data).count('#'))
        exit()

    data = new_data
