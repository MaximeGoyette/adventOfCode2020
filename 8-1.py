data = open('8.txt').read().split('\n')

import re

accumulator = 0
i = 0

seen = set()

while True:
    if i in seen:
        print(accumulator)
        exit()
    seen.add(i)
    line = data[i]
    if line.startswith('acc'):
        accumulator += int(line.split()[1].replace('+', ''))
    elif line.startswith('jmp'):
        i += int(line.split()[1].replace('+', '')) - 1
    elif line.startswith('nop'):
        pass
    i += 1
