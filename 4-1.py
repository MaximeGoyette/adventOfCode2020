data = [x.split('\n') for x in open('4.txt').read().split('\n\n')]

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

total = 0

for d in data:
    f = {*fields}
    for line in d:
        f -= set([b.split(':')[0] for b in line.split()])
    if len(f) == 0:
        total += 1

print(total)
