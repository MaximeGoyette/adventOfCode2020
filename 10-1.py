data = [int(x) for x in open('10.txt').read().split('\n')]

s = sorted([0] + data + [max(data) + 3])

a = {1:0, 2:0, 3:0}

for x, y in zip(s[:-1], s[1:]):
    a[y - x] += 1

print(a)
