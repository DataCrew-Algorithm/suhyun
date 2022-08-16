# DP: 동적계획법을 이용한 풀이

import sys
input = sys.stdin.readline

n = int(input())

tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))
# print(tri)

for i in range(1, n):   # 위의 층부터 n개의 층을 차례로 돌면서
    for j in range(len(tri[i])):        # i층의 길이만큼 돈다.
        if j-1 < 0:                     # 각층에서의 위치가 왼쪽 끝에 있는 숫자일 때
            tri[i][j] += tri[i-1][j]    # 위층 맨 왼쪽에만 영향받음
            # print(tri[i])

        elif j == len(tri[i]) - 1:      # 오른쪽 끝에 있는 숫자일 때
            tri[i][j] += tri[i-1][j-1]  # 위층 맨 오른쪽에만 영향받음
            # print(tri[i])

        else:   # 중간에 있는 숫자일 때
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])    # 위층 오른쪽 왼쪽에서 큰 숫자를 더해줌
            # print(tri[i])

print(max(tri[-1])) # 마지막 줄에서 가장 큰 숫자를 출력




