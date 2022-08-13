# DP: 동적계획법을 이용한 풀이

import sys
input = sys.stdin.readline

n = int(input())

tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))
# print(tri)

for i in range(1, n):
    for j in range(len(tri[i])):
        if j-1 < 0:             # 왼쪽 끝에 있는 숫자일 때
            tri[i][j] += tri[i-1][j]
            # print(tri[i])

        elif j == len(tri[i]) - 1: # 오른쪽 끝에 있는 숫자일 때
            tri[i][j] += tri[i-1][j-1]
            # print(tri[i])
        else:   # 중간에 있는 숫자일 때
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])
            # print(tri[i])

print(max(tri[-1]))




