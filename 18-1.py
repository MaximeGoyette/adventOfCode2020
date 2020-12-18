import re
data = open('18.txt').read().split('\n')
total = 0

for exp in data:
    exp = '(' + exp + ')'

    while '(' in exp:
        m1 = re.findall(r'\([^\(\)]+\)', exp)

        for m in m1:
            mm = m[1:-1].split()
            x = mm[0]
            n = [mm[i:i+2] for i in range(1, len(mm), 2)]

            for op, y in n:
                x = eval(str(x) + op + y)
            
            exp = exp.replace(m, str(x))

    total += int(exp)

print(total)
