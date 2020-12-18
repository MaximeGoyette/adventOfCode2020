data = [x.split('\n') for x in open('6.txt').read().split('\n\n')]

total = 0

for group in data:
    a = {l:0 for l in 'abcdefghijklmnopqrstuvwxyz'}
    for person in group:
        for ans in person:
            a[ans] += 1

    total += len([x for x, y in a.items() if y == len(group)])

print(total)
