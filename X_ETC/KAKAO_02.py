# def solution(queue1, queue2):
#     queue1_ = queue1.copy()
#     queue2_ = queue2.copy()
    
#     counter = 0
#     while True:

#         if (queue1_ == queue1)  & (queue2_ == queue2) & (counter != 0):
#             counter = -1
#             break

    
#         else:
#             if sum(queue1_) > sum(queue2_):
#                 tmp = queue1_.pop(0)
#                 queue2_.append(tmp)
#                 counter += 1

#             elif sum(queue1_) < sum(queue2_):
#                 tmp = queue2_.pop(0)
#                 queue1_.append(tmp)
#                 counter += 1

#             else:
#                 break
    
#     print(queue1_)
#     print(queue2_)
#     answer = counter
#     return answer

# # queue1 = [3, 2, 7, 2]
# # [1, 1]

# queue1 =[1, 1]
# queue2 =[1, 5]

# # queue1 = [1, 2, 1, 2]
# # queue2 = [1, 10, 1, 2]
# # queue2 = [4, 6, 5, 1]
# print(solution(queue1, queue2))



## collections이용
# from collections import deque

# def solution(queue1, queue2):
    
    
#     queue1_ = queue1[:]
#     queue2_ = queue2[:]

#     queue1 = deque(queue1)
#     queue2 = deque(queue2)


#     queue1_ = deque(queue1_)
#     queue2_ = deque(queue2_)

    
#     answer = 0
#     sum1 = sum(queue1_)
#     sum2 = sum(queue2_)

#     while True:
 
#         if answer == len(queue1_) * 2 + len(queue2_) * 2:
#         # if (queue1_[0] == queue1[0]) & (answer != 0):


#             answer = -1
#             break
  

#         else: 
#             if sum1 > sum2:
#                 tmp = queue1_.popleft()
#                 sum1 -= tmp
#                 sum2 += tmp
#                 queue2_.append(tmp)
#                 answer += 1

#             elif sum1 < sum2:
#                 tmp = queue2_.popleft()
#                 sum2 -= tmp
#                 sum1 += tmp
#                 queue1_.append(tmp)
#                 answer += 1

#             else:
#                 break
    
#     print(queue1_)
#     print(queue2_)
#     return answer

# queue1 = [1, 2, 1, 2]
# queue2 = [1, 10, 1, 2]

# # queue1 =[1, 1]
# # queue2 =[1, 5]

# print(solution(queue1, queue2))


# 절반 추가

from collections import deque

def solution(queue1, queue2):
    
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    answer = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    target = (sum1+sum2)/2  # 두 큐가 같아지려면, 전체 합을 2로 나눴을 경우가 되어야 한다.

    while True:
        if not queue2:     # 두번째 큐가 비었을 때, 반바퀴 돈 것이며, 이 때까지 돌았다는 것은 만족하는 값이 없다는 뜻
            answer = -1
            break
            
        else:                   # target만 맞추면 되므로 하나의 큐만 비교하면 됨
            if sum1 > target:               # 클 때는 빼주고
                tmp = queue1.popleft()
                sum1 -= tmp
                answer += 1

            elif sum1 < target:             # 작을때는 더해주고
                tmp = queue2.popleft()
                sum1 += tmp
                queue1.append(tmp)
                answer += 1

            else:                           # 같으면 종료
                break
    

    return answer

# queue1 = [1, 2, 1, 2]
# queue2 = [1, 10, 1, 2]

queue1 =[1, 1]
queue2 =[1, 5]

print(solution(queue1, queue2))



# from collections import deque

# def solution(queue1, queue2):
    
    
#     queue1_ = queue1[:]
#     queue2_ = queue2[:]

#     queue1 = deque(queue1)
#     queue2 = deque(queue2)


#     queue1_ = deque(queue1_)
#     queue2_ = deque(queue2_)

    
#     answer = 0
#     sum1 = sum(queue1_)
#     sum2 = sum(queue2_)
#     target = (sum1+sum2)/2  # 두 큐가 같아지려면, 전체 합을 2로 나눴을 경우가 되어야 한다.

#     while True:
#         if not queue2_:     # 두번째 큐가 비었을 때, 반바퀴 돈 것이며, 이 때까지 돌았다는 것은 만족하는 값이 없다는 뜻
#             answer = -1
#             break
            
#         else:                   # target만 맞추면 되므로 하나의 큐만 비교하면 됨
#             if sum1 > target:               
#                 tmp = queue1_.popleft()
#                 sum1 -= tmp
#                 answer += 1

#             elif sum1 < target:
#                 tmp = queue2_.popleft()
#                 sum1 += tmp
#                 queue1_.append(tmp)
#                 answer += 1

#             else:
#                 break
    

#     return answer