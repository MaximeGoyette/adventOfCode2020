data = open('3.txt').read().split('\n')

trees = 0

x = y = 0

while y < len(data):
    x += 3
    y += 1
    if y >= len(data):
        break

    if data[y][x%len(data[0])] == '#':
        trees += 1

print(trees)
