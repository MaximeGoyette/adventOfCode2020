data = [x.split('\n') for x in open('4.txt').read().split('\n\n')]

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

total = 0

for d in data:
    f = {*fields}
    for line in d:
        for xx in line.split():
            field, value = xx.split(':')
            if field == 'byr' and 1920 <= int(value) <= 2002:
                f.remove(field)
            if field == 'iyr' and 2010 <= int(value) <= 2020:
                f.remove(field)
            if field == 'eyr' and 2020 <= int(value) <= 2030:
                f.remove(field)
            if field == 'hgt':
                if value.endswith('cm') and 150 <= int(value[:-2]) <= 193:
                    f.remove(field)
                if value.endswith('in') and 59 <= int(value[:-2]) <= 76:
                    f.remove(field)
            if field == 'hcl' and value[0] == '#' and len(value) == 7 and all([c.lower() in '0123456789abcdef' for c in value[1:]]):
                f.remove(field)
            if field == 'ecl' and value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                f.remove(field)
            if field == 'pid' and len(value) == 9 and all([c.isdigit() for c in value]):
                f.remove(field)
    if len(f) == 0:
        total += 1

print(total)
