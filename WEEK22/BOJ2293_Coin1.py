# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())

# coins = [int(input()) for _ in range(n)]
# tmp = []
# for coin in coins:
#     tmp.append(k // coin)

# print(tmp)

# 블로그 풀이
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
dp = [0 for i in range(k+1)]
dp[0] = 1

for i in coins:
    for j in range(i, k+1): # i부터 목표값인 k까지의 dp를 계속 갱신해나감. i이전 값들은 어차피 0이라 i부터 출발
        if j - i >= 0:
            dp[j] += dp[j-i]
print(dp[k])
# https://mong9data.tistory.com/68
# https://velog.io/@ready2start/Python-%EB%B0%B1%EC%A4%80-2293-%EB%8F%99%EC%A0%84-1
# https://seongonion.tistory.com/108

'''
  1 2 3 4 5 6 7 8 9 10
1 1 1 1 1 1 1 1 1 1 1
2 0 1 1 2 2 3 3 4 4 5
5 0 0 0 0 1 1 2 2 3 4
t 1 2 2 3 4 5 6 7 8 10 
'''
