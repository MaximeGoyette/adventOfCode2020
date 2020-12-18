def is_valid(policy, passwd):
    # 17-19 c: hvchccvccdxgccnxdcc
    pass

total = 0
for x in open('2.txt').read().split('\n'):
    n1, n2 = x.split(' ')[0].split('-')
    l = x.split(' ')[1][:-1]
    p = x.split(' ')[-1]


    if int(p[int(n1) - 1] == l) + int(p[int(n2) - 1] == l) == 1:
        total += 1

print(total) 