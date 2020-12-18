from itertools import product

data = open('14.txt').read().split('\n')

mask = None
mem = {}

for line in data:
    if line.startswith('mask'):
        mask = [int(x) if x != 'X' else 'X' for x in line.split(' = ')[1].zfill(36)]
    else:
        n = [int(x) for x in bin(int(line.split('[')[1].split(']')[0]))[2:].zfill(36)]

        value = int(line.split(' = ')[1])

        possible_ns = [{'X': [0, 1], 0: [a], 1: [1]}[b] for a, b in zip(n, mask)]

        for possible_n in product(*possible_ns):
            mem[int(''.join(map(str,possible_n)), 2)] = value


print(sum(mem.values()))
