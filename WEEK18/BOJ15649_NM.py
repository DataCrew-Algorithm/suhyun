import sys
from itertools import permutations

read = sys.stdin.readline

N, M = map(int, read().split())

perm = list(permutations([i for i in range(1, N+1)], M)) 
# 순열 => 리스트안에 튜플로 받아줌

for i in perm:
    print(*i) # 튜플 빠져나오기 위한 언패킹


