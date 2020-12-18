data = [int(x) for x in open('10.txt').read().split('\n')]

from itertools import product
from functools import lru_cache

data = [0] + [*sorted(data)] + [max(data) + 3]
l = len(data)

def find_candidates(i):
    candidates = set()
    for j in range(i + 1, l):
        if data[j] - data[i] < 4:
            candidates.add(j)
        else:
            break
    return candidates

target = data[-1]

@lru_cache(None)
def count(i):
    if data[i] == target:
        return 1
    else:
        total = 0
        for candidate in find_candidates(i):
            total += count(candidate)
        return total

print(count(0))
