data = open('12.txt').read().split('\n')

waypoint = [10, -1]
position = [0, 0]

for line in data:
    i, n = line[0], int(line[1:])
    if i == 'N':
        waypoint[1] -= n
    elif i == 'S':
        waypoint[1] += n
    elif i == 'E':
        waypoint[0] += n
    elif i == 'W':
        waypoint[0] -= n
    elif i == 'L':
        for _ in range(n//90):
            waypoint = [waypoint[1], -waypoint[0]]
    elif i == 'R':
        for _ in range(n//90):
            waypoint = [-waypoint[1], waypoint[0]]
    elif i == 'F':
        position = [position[0] + waypoint[0]*n, position[1] + waypoint[1]*n]

print(abs(position[0]) + abs(position[1]))
