data = open('5.txt').read().split('\n')

m = 0

ids = set()

for seat in data:
    row = int(seat[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(seat[-3:].replace('L', '0').replace('R', '1'), 2)
    _id = row*8+col
    ids.add(_id)


i = min(ids) + 1
while True:
    if i not in ids and i - 1 in ids and i + 1 in ids:
        print(i)
        exit()
    i += 1