data = open('9.txt').read().split('\n')
data = [int(x) for x in data]

target = 70639851

for i in range(len(data)):
    for j in range(i+1, len(data)):
        if sum(data[i:j+1]) == target:
            print(min(data[i:j+1]) + max(data[i:j+1]))
            exit()
