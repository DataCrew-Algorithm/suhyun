# import sys
# from collections import deque
# read = sys.stdin.readline

# n = int(read())
# target = [int(read()) for _ in range(n)]

# print(target)

# q = deque([i for i in range(1, n+1)])

# print(q)
# stack = []


# for i in target:
#     while True:
#         if not stack:
#             stack.append(q.popleft())
#             print('+')

#         if i == stack[-1]:
#             break

#         else:
#             stack.append(q.popleft())
#             print('+')


#     q.append(stack.pop())
#     print('-')


# No를 고려한 풀이

import sys
from collections import deque
read = sys.stdin.readline

n = int(read())
target = [int(read()) for _ in range(n)]    # 만들고 싶은 수열을 입력 받음

# print(target)

q = deque([i for i in range(1, n+1)])       # 초기 queue를 만들어 놓음
# print(q)

stack = []
result = []

try:   # NO로 출력해야하는 부분을 위한 try/except
    for i in target:
        while True:
            if not stack:
                stack.append(q.popleft())
                result.append('+')

            if i == stack[-1]:
                break

            else:
                stack.append(q.popleft())
                result.append('+')


        q.append(stack.pop())
        result.append('-')
    
    for i in result: # NO를 위해서 가능한 경우에는 result에 담아놓음
        print(i)    # 순서대로 출력
except:
    print('NO')

'''
target = [4,3,6,8,7,5,2,1] => 목표 리스트

stack = [] <-임시로 담아두는 스택

queue <- 12345678 로 시작

s 1234
q 5678

s 123
q 56784

s 12
q 567843

'''
    

            



