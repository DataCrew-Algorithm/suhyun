# # 시간초과
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10000)

# T = int(input())

# def fibonacci(n):
#     if n == 0:
#         return [1, 0]
#     elif n == 1:
#         return [0, 1]
#     else:           # 각 인덱스의 합을 출력하는 함수
#         return [fibonacci(n-1)[i] + fibonacci(n-2)[i] for i in range(2)]
        

# for _ in range(T):
#     tmp = int(input())
#     print(fibonacci(tmp))


# 시간초과 - 문제: 메모리에 저장해둬서 했던 작업 반복하지 않게 해야함
# import sys
# input = sys.stdin.readline

# T = int(input())

# def f1(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 0
#     else:
#         return f1(n-1) + f1(n-2)

# def f2(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return f2(n-1) + f2(n-2)
        

# for _ in range(T):
#     tmp = int(input())
#     print(f1(tmp), f2(tmp))

# 블로그 풀이 - 했던 행위를 메모리에 넣고, 또 다시 반복하지 않음
import sys
input = sys.stdin.readline

T = int(input())
zero = [1, 0, 1]
one = [0, 1, 1]

def fibonacci(n):
    length = len(zero)                          # 지금까지 완성된 길이만큼 적는다.
    if n >= length:                             # 그것보다 더 크다면,
        for i in range(length, n+1):            # 지금까지 완성된 것 이후의 값을 채워 넣는다.
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])     
    return zero[n], one[n]


for _ in range(T):
    print(*fibonacci(int(input())))


'''
f(0) = 0				        1 0
f(1) = 1				        0 1
f(2) = 0+1			            1 1
f(3) = 2 = 1+(0+1)			    1 2
f(4) = 3 = (0+1)+1+(0+1)		2 3
f(5) = 5 = 1 *2  + (0+1) * 3	3 5
f(6) = 8				        5 8
'''