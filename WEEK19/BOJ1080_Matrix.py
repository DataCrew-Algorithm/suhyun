# import sys
# read = sys.stdin.readline

# N, M = map(int, read().split())

# A = []
# B = []
# for _ in range(N):
#     A.append(list(read().rstrip()))

# for _ in range(N):
#     B.append(list(read().rstrip()))


# def cal(m):
#     for i in range(3):
#         for j in range(3):
#             if i[j] == 1:
#                 i[j] = 0
#             else:
#                 i[j] = 1


# 블로그 풀이
from sys import stdin

N, M = map(int, stdin.readline().split())
A = [list(map(int, stdin.readline().rstrip())) for j in range(N)]
B = [list(map(int, stdin.readline().rstrip())) for j in range(N)]
cnt = 0


def flip(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            A[x][y] = 1 - A[x][y]


# i, j 는 3x3행렬의 맨왼쪽위 기준점임
for i in range(N - 2):  # 기준점이 세로 이동가능 횟수
    for j in range(M - 2):  # 기준점이 가로로 이동 가능 횟수
        if A[i][j] != B[i][j]:
            flip(i, j)
            cnt += 1

        if A == B:
            break
    if A == B:
        break

if A != B:
    print(-1)
else:
    print(cnt)


'''
CNN에서 kernel을 대는 느낌
좌상단만 비교하는 이유는, 다른것이 어떻든 상관이 없음. 좌상단끼리만 비교해서 바꿨는데
결과적으로 A B가 다르다면 그냥 안되는 놈이었던 것임
'''
