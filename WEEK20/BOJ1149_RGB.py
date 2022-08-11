# import sys
# input = sys.stdin.readline

# # 0, 1, 2 담아놓고, 이전에 것과 다른것으로 계속해서 반복
# def redundancy(a):
#     if a == 0:
#         return [1,2]
#     elif a == 1:
#         return [0,2]
#     else:
#         return [0,1]

# # 탐색하는 알고리즘 짜다가 실패..
# def dfs():


# N = int(input())
# costs = []
# for _ in range(N):
#     costs.append(list(map(int, input().split())))


# for _ in range(N):


# print(costs)

# 블로그 풀이 -> 동적계획법

import sys
read = sys.stdin.readline

N = int(read())
cache =[list(map(int, read().split())) for _ in range(N)]
print(cache)
for i in range(1, N):
    cache[i][0] += min(cache[i-1][1], cache[i-1][2])    # 출발점이 0인 것
    cache[i][1] += min(cache[i-1][0], cache[i-1][2])    # 출발점이 1인 것
    cache[i][2] += min(cache[i-1][0], cache[i-1][1])    # 출발점이 2인 것
print(min(cache[-1]))

'''
두번째 집의 첫번째 49에는 앞서 40, 83에서만 와야했으므로, 그 중에서 작은 값을 더해줌
'''



