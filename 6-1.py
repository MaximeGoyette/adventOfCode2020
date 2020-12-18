data = [x.split('\n') for x in open('6.txt').read().split('\n\n')]

total = 0

for group in data:
    a = set()
    for person in group:
        for ans in person:
            a.add(ans)

    total += len(a)

print(total)
