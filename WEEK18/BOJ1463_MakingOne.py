# 틀린 풀이..
import sys
read = sys.stdin.readline

N = int(read())
a, b, c = -1, -1, N+1
result = N

# 3 ** a + 2 ** b + c

while 3 ** a < N:
    a += 1
    b = -1
    while 2 ** b < N:
        b += 1
        c = N+1
        while c > 0 :
            c -= 1
            if (a == 0) & (b != 0):
                M = 2 ** b + c 
            elif (b == 0) & (a != 0):
                M = 3 ** a + c
            elif (a == 0) & (b == 0):
                M = c
            else: M = 3 ** a + 2 ** b + c

            if M == N:
                print(a,b,c)
                result = min(result, a + b + c) # 모든 경우를 포괄하지 못함

print(result)


# ver2 3과 2의 공배수일때는 순차적으로 하는 방식을 채택..
import sys
read = sys.stdin.readline

N = int(read())
a, b, c = 0, 0, 0
result = N

def judge(x): # 3으로 나눠떨어지면서, 2로 나눠떨어질때는 순차적으로 해야함
    if x % 3 == 0:
        if x % 2 != 0:
            n = x / 3
        else:
            judge(n)
    elif x % 2 == 0:
        n = x / 3
    
    else: 
        n = x - 1

def div3(x):
    if x % 3 == 0:
        return x/3
    else: return x

def div2(x):
    if x % 2 == 0:
        return x/2

def minus1(x):
    return x-1

# ver 3 동적계획법 풀이 -> 점화식을 떠올려서 푼다.
import sys
read = sys.stdin.readline
n = int(read())

dp = [0] * (n+1)

for i in range(2, n+1): # 3개를 모두 판별해서 
    dp[i] = dp[i-1] + 1 # 먼저 1을 더하고 시작

    if i % 2 == 0:  # 2로 나누어 떨어질 때, 
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:  # 3으로 나누어 떨어질 때, 
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])


'''
2로 갈때
dp[10] = dp[5] + 1 = 3 + 1 = 4
dp[5] = dp[4] + 1 = 2 + 1
dp[4] = dp[2] + 1 = 1 + 1
dp[2] = dp[1] + 1 = 0 + 1

1로 갈때
dp[10] = dp[9] + 1 = 2 + 1 = 3
dp[9] = dp[3] + 1 = 1 + 1
dp[3] = dp[1] + 1 = 0 + 1
'''