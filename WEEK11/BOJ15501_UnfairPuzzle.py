# 1200ms 많이 느림

# 뒤집기는 구성이 바뀌는 것이 아니므로 고려하지 않음. 
# -> 밀기만 고려

# from collections import deque
# n = input()

# nums1 = list(map(int, input().split(' ')))
# nums2 = list(map(int, input().split(' ')))

# deque1 = deque(nums1)
# deque2 = deque(nums2)
# deque2_rev = deque(reversed(deque2)) # 원본은 보존하기 위해, 뒤집은 것을 새로 담음
# i = 0                                

# # 목표가 되는 queue2는 가만히 두고, queue1만 밀기 연산 할 것임
# while i != len(deque1): # 밀기를 수열 길이만큼 하면 제자리로 돌아온 것이므로 종료

#     if (deque1 == deque2) or (deque1 == deque2_rev): # 원본이나, 뒤집기 한 것이나 같으면 종료
#         print('good puzzle')
#         break

#     else:
#         tmp = deque1.popleft()
#         deque1.append(tmp)
#         i += 1                  # 밀기 연산을 한 횟수 count
#         # print(deque1)

# if i == len(deque1):            # 밀기를 수열의 길이만큼 돌았는데도 안나온 것이므로 bad
#     print('bad puzzle')


# ------------------------------------------------------
# 느렸던 원인 찾음: map으로 int로 바꿔주는 과정에서 300ms나 잡아먹음.
from collections import deque
n = input()

deque1 = deque(input().split(' ')) # 굳이 int로 안바꿔줘도 되면 하지말자!!
deque2 = deque(input().split(' '))


deque2_rev = deque(reversed(deque2)) # 원본은 보존하기 위해, 뒤집은 것을 새로 담음
i = 0                                

# 목표가 되는 queue2는 가만히 두고, queue1만 밀기 연산 할 것임
while i != len(deque1): # 밀기를 수열 길이만큼 하면 제자리로 돌아온 것이므로 종료

    if (deque1 == deque2) or (deque1 == deque2_rev): # 원본이나, 뒤집기 한 것이나 같으면 종료
        print('good puzzle')
        break

    else:
        deque1.rotate(1)
        
        i += 1                  # 밀기 연산을 한 횟수 count
        # print(deque1)

if i == len(deque1):            # 밀기를 수열의 길이만큼 돌았는데도 안나온 것이므로 bad
    print('bad puzzle')