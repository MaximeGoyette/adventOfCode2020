directions = [
    (1, 0),
    (0, -1),
    (-1, 0),
    (0, 1),
]

direction = 0

data = open('12.txt').read().split('\n')

position = [0, 0]

for line in data:
    i, n = line[0], int(line[1:])
    if i == 'N':
        position[1] -= n
    elif i == 'S':
        position[1] += n
    elif i == 'E':
        position[0] += n
    elif i == 'W':
        position[0] -= n
    elif i == 'L':
        direction = (direction - 1)%len(directions)
        d = directions[direction]
        position = [position[0] + d[0], position[1] + d[1]]
    elif i == 'R':
        direction = (direction + 1)%len(directions)
        d = directions[direction]
        position = [position[0] + d[0], position[1] + d[1]]
    elif i == 'F':
        d = directions[direction]
        position = [position[0] + d[0], position[1] + d[1]]

print(abs(position[0]) + abs(position[1]))
