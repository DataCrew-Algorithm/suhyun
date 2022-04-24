# # ver1 시간초과
# n = int(input())

# for i in range((n//5) +1, 0, -1):
#     for j in range(1, (n//2)+1):
#         if 5*i - n == j:
#             print(i+j)
#             break
#             break
# if (i == 1 & j == n//2) & (5 * i - n != j):
#     print(-1)

# ver2
n = int(input())

if n == 1 or n == 3:    # 5보다 작은 수 중 2의 배수가 아닌 수들 -1로
    print(-1)
# 5x + 2y = n
for x in range((n//5), -1, -1):
    y = n - 5 * x
    if y % 2 == 0:
        print(x+(y//2))
        break

if (x == 1 & y == n//2) & (5 * x - n != y): # 다 돌았는데도 성립하지 않는 경우
    print(-1)

