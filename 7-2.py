
data = open('7.txt').read().split('\n')

from collections import defaultdict

bags = defaultdict(list)

for line in data:
    a, b = line.split(' bags contain ')
    c = [(int(x.split()[0].replace('no', '0')), ' '.join(x.split()[1:-1])) for x in b.split(', ')]
    for n, name in c:
        bags[a].append((n, name))

target = 'shiny gold'

n = 0

def count(target, mult=1):
    global bags, n
    for c, name in bags.get(target, []):
        n += c*mult
        count(name, mult=mult*c)

count(target)
print(n)
