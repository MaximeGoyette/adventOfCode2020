
data = open('7.txt').read().split('\n')

from collections import defaultdict

bags = defaultdict(list)

for line in data:
    a, b = line.split(' bags contain ')
    c = [(int(x.split()[0].replace('no', '0')), ' '.join(x.split()[1:-1])) for x in b.split(', ')]
    for n, name in c:
        bags[name].append(a)

target = 'shiny gold'

n = set()

def count(target):
    if target is None:
        return
    else:
        global n, bags
        n.add(target)
        for b in bags.get(target, []):
            count(b)

count(target)

print(len(n) - 1)
