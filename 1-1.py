data = open('1.txt').read().split('\n')

from itertools import product
for a, b in product(data, repeat=2):
    if int(a) + int(b) == 2020:
        print(int(a)*int(b))
