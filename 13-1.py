data = open('13.txt').read().split('\n')

t = int(data[0])
buses = [int(x) for x in data[1].split(',') if x != 'x']

i = t

while True:
    for b in buses:
        if i%b == 0:
            print((i - t)*b)
            exit()
    i += 1
