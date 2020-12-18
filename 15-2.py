numbers = [0,13,16,17,1,10]
current = 6
seen_at = {x:i for i, x in enumerate(numbers)}

for i in range(len(numbers), 30000000):
    if current in seen_at:
        s = i - seen_at[current]
    else:
        s = 0
    seen_at[current] = i
    numbers.append(current)
    current = s

print(numbers[-1])
