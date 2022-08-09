import sys
input = sys.stdin.readline

N, K, L = map(int, input().split())

def check_div(num):
    if num % 2 == 0:
        result = num//2
    else:
        result = num//2 + 1
    return result


cnt = 0
while K != L:
    cnt += 1
    K = check_div(K)
    L = check_div(L)

print(cnt)

        

