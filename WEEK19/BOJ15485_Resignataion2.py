# import sys
# read = sys.stdin.readline

# N = int(read())

# days = []
# revenues = []

# for _ in range(N):
    
#     D, R = map(int, read().rstrip().split())
#     days.append(D)
#     revenues.append(R)


# idx = 0
# sum_rev = 0
# sum_a = []

# for i in range(N):
#     idx = i
#     sum_rev = revenues[i]

#     while (idx + days[idx]< N) & (idx < N):
#         idx += days[idx]
#         sum_rev += revenues[idx]
#     sum_a.append(sum_rev)

# print(sum_a)

'''

idx
0 -> 3 -> 4

revenues
10   20    15

days
3      1    2   

여러 루트로 가는 것을 구현 x
[245, 220, 245, 235, 215, 40, 200]
'''

# 블로그 풀이 참고
import sys 
read = sys.stdin.readline 

n = int(read())
days,revenues = [],[]
dp = [0] * (n+1)            # [0, 0, 0, 10, 30, 0, 45, 0]
for i in range(n):
    x,y = map(int,read().split())
    days.append(x)
    revenues.append(y)
M = 0                       # 누적 수익 M
for i in range(n):          # i에서 출발하는 최대 수익을 가진 루트로 계속 갱신
    M = max(M, dp[i])  
    if i + days[i] > n :    # index가 넘어설 때는 for문 위로 돌아감
        continue
    dp[i+days[i]] = max(M + revenues[i], dp[i+days[i]]) 
    # 이동할 다음 루트의 원래 값과 새로운 수익을 더한값중 큰 값으로 대체
# print(dp)
print(max(dp))




