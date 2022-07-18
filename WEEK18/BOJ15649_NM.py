import sys
from itertools import permutations

read = sys.stdin.readline

N, M = map(int, read().split())

perm = list(permutations([i for i in range(1, N+1)], M))

for i in perm:
    print(*i)


