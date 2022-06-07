# 함수 정의
def sum_re(lst):
    result = 0
    for i in range(len(lst)):
        result += lst[i] * (len(lst)-i)
    return result

import sys
N = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
p = sorted(p)
print(sum_re(p))


