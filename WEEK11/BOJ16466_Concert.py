# 시간초과..
# import sys
# N = input()
# nums_sold = list(map(int, sys.stdin.readline().split()))
# # [4, 1, 2, 7, 8]
# i = 0
# while True:
#     i += 1
#     if i in nums_sold:
#         continue
#     else:
#         print(i)
#         break
# import heapq

# ver2
# import sys
# N = input()
# nums_sold = list(map(int, sys.stdin.readline().split()))
# i = 0
# if min(nums_sold) != 1:
#     print(1)

# else:
#     while True:
#         i += 1
#         if i in nums_sold:
#             continue
#         else:
#             print(i)
#             break

# 인터넷에 나온 풀이..
import sys

N = int(sys.stdin.readline())
sold = sorted(list(map(int, sys.stdin.readline().split())))

# 1 2 4 7 8
# 1 2 3 4 5 두 배열의 각 원소를 순서대로 비교해나감. 서로 값이 다를 경우 해당 순서의 자리가 빈 것
for i in range(1,N+1) :
    if(sold[i-1] != i) :
        print(i)
        sys.exit()
else: # break 안걸렸을때 실행.
    print(N+1)


#배열 중간에 빈 자리가 없는 경우
