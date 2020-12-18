data = open('1.txt').read().split('\n')

from itertools import product
for a, b, c in product(data, repeat=3):
    if int(a) + int(b) + int(c) == 2020:
        print(int(a)*int(b)*int(c))
