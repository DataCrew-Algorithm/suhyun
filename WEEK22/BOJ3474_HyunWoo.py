import sys
input = sys.stdin.readline

T = int(input())

# 0 의 개수는 소인수분해 했을 때, 10(=2*5)의 개수가 몇개인지 알면 됨
def checker(N): # 2^x * 5^y *..
    cnt_2 = 0
    cnt_5 = 0
    while True:            # 2의 개수인 x를 찾음
        if N % 2 == 0:
            N = N // 2
            cnt_2 += 1
        else: break
    while True:            # 5의 개수인 y를 찾음
        if N % 5 == 0:
            N = N // 5
            cnt_5 += 1
        else: break
    return min(cnt_2, cnt_5)

# factorial 구하는 함수 정의
dp = [1, 1]
def factorial(n):
    for i in range(len(dp), n+1):
        dp.append(dp[i-1] * i)
    return dp[n]

for _ in range(T):
    tmp = factorial(int(input()))
    print(checker(tmp))

# 블로그 풀이
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())  # 수 입력 받기
    count = 0
    i = 5
    while i <= n:
        count += n // i  # 5의 배수의 합을 구한다(2의 배수는 구할 필요가 없음.)
        i *= 5
        
    print(count)