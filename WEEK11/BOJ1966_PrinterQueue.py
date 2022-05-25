import sys
from collections import deque

num_cases = int(input())

for _ in range(num_cases):
    N, M = map(int, sys.stdin.readline().split())
    sig = deque(map(int, sys.stdin.readline().split()))

    indices = deque([i for i in range(N)]) # 인덱스들을 담을 큐 0 ~ N-1
    print_idx = -1                          # 인덱스가 0부터 시작하므로 겹치지 않게 -1로 초기화
    counter = 0

    # sig와 indices를 같은 작업을 반복함
    while print_idx != M: # 빼낸 인덱스가 타겟인 M과 같아질때 까지
        counter += 1
        # print(sig)
        max_sig = max(sig)
        idx = sig.index(max_sig)
        sig.rotate(-idx)            # rotate함수의 반시계 방향 돌리기 위해 - 붙임
        indices.rotate(-idx)
        sig.popleft()
        print_idx = indices.popleft()
        # print(print_idx)
    print(counter)



    




