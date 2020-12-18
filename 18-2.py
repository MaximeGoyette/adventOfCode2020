import re

data = open('18.txt').read().split('\n')
total = 0

for exp in data:
    exp = '(' + exp.replace(' ', '') + ')'

    while '(' in exp:
        m1 = re.findall(r'\([^\(\)]+\)', exp)

        for m in m1:
            mm = re.sub(r'([\d\+]+)', r'(\g<1>)', m[1:-1])
            exp = exp.replace(m, str(eval(mm)))

    total += int(exp)

print(total)
