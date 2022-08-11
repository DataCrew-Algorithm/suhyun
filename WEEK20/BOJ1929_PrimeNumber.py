# # 시간초과
# import sys

# input = sys.stdin.readline

# M, N = map(int, input().split())

# for i in range(M, N+1):
#     for j in range(2, i):
#         if i % j == 0:      # 나누어 떨어진다. = 소수가 아니다.
#             break
#     else:
#         print(i)

# 블로그 힌트 -> i의 제곱근까지만 하면 됨

# 시간초과
import sys

input = sys.stdin.readline

M, N = map(int, input().split())

for i in range(M, N+1):
    if i == 1:  # M이 1부터 시작하므로 1일때는 안 돌아야함
        continue
    else:                   # 제곱근 까지만 구하면 됨(제곱했을 때 수 까지만 나오면 그 위는 고려할 필요가 없음)
        for j in range(2, int(i**0.5)+1):   
            if i % j == 0:      # 나누어 떨어진다. = 소수가 아니다.
                break
        else:
            print(i)