data = open('13.txt').read().split('\n')

buses = [(int(x), i) for i, x in enumerate(data[1].split(',')) if x != 'x']

from sympy.ntheory.modular import crt

c = crt(*zip(*buses))

print(c[1] - c[0])
