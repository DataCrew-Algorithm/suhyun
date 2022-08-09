import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
q = deque([i for i in range(1, N+1)]) # 1~N까지를 담은 Queue
indices = list(map(int, input().split())) # 입력 받아서 찾을 것들을 담음
result = 0

for idx in indices:
    cnt = 0
    while q[0] != idx:
        q.rotate(1)     # queue의 맨 처음 값이 목표하는 값과 다를때, 회전
        cnt += 1

    q.popleft()

    result += min(len(q)+1-cnt, cnt)    # 한 방향으로 계속 돌린 횟수 = 전체길이 - 반대 방향으로 돌린 횟수
    # popleft로 하나 제거한 뒤 이므로 +1을 함

print(result)


        
