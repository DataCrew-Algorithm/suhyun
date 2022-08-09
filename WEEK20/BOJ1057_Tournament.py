import sys
input = sys.stdin.readline

N, K, L = map(int, input().split())


# 서로 상대로 붙는다는 것은, 나눴을때 같아지는 것을 의미

def check_div(num):
    if num % 2 == 0:        # 짝수일 때, 2로 나눔
        result = num//2
    else:
        result = num//2 + 1 # 홀수일 때, 2로 나누고 +1
    return result


cnt = 0
while K != L:   # 둘이 같지 않을 때는 계속함
    cnt += 1
    K = check_div(K)
    L = check_div(L)

print(cnt)

        

