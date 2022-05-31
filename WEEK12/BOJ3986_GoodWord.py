# import sys
# N = int(sys.stdin.readline())
# counter = 0

# for _ in range(N):
#     word = list(sys.stdin.readline())
#     left = 0
#     right = 1
#     while right != len(word):
#         if word[left] + word[right] == 'AA' or 'BB':
#             print('same')
#             del(word[left])
#             print(word)
#             del(word[right])
#             print(word)
#             left = 0
#             right = 1
#         else:
#             left += 1
#             right += 1
#     print(word)
#     if len(word) == 0:
#         counter += 1

# print(counter)


#ver2
# import sys
# N = int(sys.stdin.readline())
# counter = 0

# for _ in range(N):
#     word = list(sys.stdin.readline())

#     while True:
#         if word[0] == 'A':
#             if word[1] == 'A':
#                 word.pop(0)
#                 word.pop(1)
#                 print(word)
#             elif word[-1] == 'A':
#                 word.pop(-1)
#             else:
#                 break

#         elif word[0] == 'B':
#             if word[1] == 'B':
#                 word.pop(0)
#                 word.pop(1)
#             elif word[-1] == 'B':
#                 word.pop(-1)
#             else:
#                 break
#     if len(word) == 0:
#         counter += 1

# print(counter)


# ABAB -> A -> B   -> A   -> B
# 스택  -> A -> AB -> ABA -> B

# ABAB -> A -> A   -> B   -> B
# 스택  -> A ->   -> B ->  

# ABBA -> A -> B   -> B  -> A
# 스택  -> A -> AB -> A ->   

#ver3
import sys
N = int(sys.stdin.readline())
counter = 0

for _ in range(N):
    word = sys.stdin.readline().rstrip() # \n 제거
    stack = []

    for i in range(len(word)):
        if stack:                    # 스택이 비어있지 않을때,
            if word[i] == stack[-1]: # 해당 문자와 스택에 맨 뒤에 문자가 같을 때,
                stack.pop()          # 스택에서 제거
            else:
                stack.append(word[i]) # 같지 않을 때는 스택에 추가 해줌
        else:                       # 스택이 비어있을 때
            stack.append(word[i])   # 스택에 추가

    if not stack:                   # 스택이 비어있으면
        counter += 1                

print(counter)

            