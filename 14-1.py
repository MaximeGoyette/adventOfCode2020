data = open('14.txt').read().split('\n')

mask = None
mem = {}

for line in data:
    if line.startswith('mask'):
        mask = [int(x) if x != 'X' else 'X' for x in line.split(' = ')[1].zfill(36)]
    else:
        n = int(line.split('[')[1].split(']')[0])
        value = [int(x) for x in bin(int(line.split(' = ')[1]))[2:].zfill(36)]
        mem[n] = [b if b != 'X' else a for a, b in zip(value, mask)]


print(sum([int(''.join(map(str,x)), 2) for x in mem.values()]))
