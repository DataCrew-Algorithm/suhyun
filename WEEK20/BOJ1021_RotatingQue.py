import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
q = deque([i for i in range(1, N+1)])
indices = list(map(int, input().split()))
result = 0
for idx in indices:
    cnt = 0
    while q[0] != idx:
        q.rotate(1)
        cnt += 1

    q.popleft()

    result += min(len(q)+1-cnt, cnt)

print(result)


        
