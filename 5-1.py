data = open('5.txt').read().split('\n')

m = 0

for seat in data:
    row = int(seat[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(seat[-3:].replace('L', '0').replace('R', '1'), 2)
    _id = row*8+col
    if _id > m:
        m = _id

print(m)
