# # ver1 전체 다 탐색해서 느림
# n = int(input())
# counter = 0

# num_list = list(map(int, input().split()))
# target = int(input())

# for i in range(n-1):
#     for j in range(i+1, n):
#         if num_list[i] + num_list[j] == target:
#             counter += 1

# print(counter)

# # ver2


# n = int(input())
# counter = 0

# num_list = list(map(int, input().split()))
# target = int(input())
# i = 0
# num_list.sort()

# new_list = []

# # if target < num_list[0]:
# #     print(0)
# # else:
# while True:
#     if (num_list[i] >= target) or (i == n-1):
#         break    
#     else: 
#         i += 1
#         # print(i)
# new_list = num_list[:i+1]
# # print(new_list)
# # for i in range(len(new_list)-1):
# #     for j in range(i+1, len(new_list)):
# #         if new_list[i] + new_list[j] == target:
# #             counter += 1

# # ???if target >= new_list[0]:
# #     if n == 2 & sum(new_list) == target:
# #             print(1)


# if sum(new_list[-2:]) <= target:
#     print(0)

# else:
#     for i in range(round((len(new_list)/2)+0.1)):
#         for j in range(i+1, len(new_list)):
#             if (target - new_list[i]) == new_list[j]:
#                 counter += 1
#                 break
                

#     if ((target / 2) in new_list) & n >= 2:
#         counter -= 1


#     print(counter)


# 7 8 9 10 11 12-> target 5일 때, 문제 발생 해결



# # ver3
# n = int(input())
# num_list = list(map(int, input().split()))
# num_list.sort()
# target = int(input())
# i = 0
# # ans_list = []
# counter = 0
# # print(num_list)
# if num_list[0] >= n:
#     print(0)

# elif (num_list[0] <= n) & (num_list[1] >= n):
#     print(0)

# else:
#     while True:
#         if target//2 < num_list[i]:
#             break
#         else:
#             i += 1
#     for j in range(i-1):
#         for k in range(i, len(num_list)):
#             if (target - num_list[j]) == num_list[k]:
#                 # if num_list[j] != (target - num_list[j]):
#                 counter += 1
#                 break
#     print(counter)

    
# # ver4: 투 포인터 이용
# n = int(input())
# num_list = list(map(int, input().split()))
# num_list.sort()
# target = int(input())
# i = 0
# # ans_list = []
# counter = 0
# # print(num_list)

# # while True:
# #     if target//2 < num_list[i]:
# #         break
# #     else:
# #         i += 1

# # start = i-1
# # end =  i
# # print(num_list)
# start = 0
# end = 1
# # while num_list[end] < n:
# #     if num_list[start] + num_list[end] < target:
# #         end += 1

# #     elif num_list[start] + num_list[end] > target:
# #         start -= 1
    
# #     else:
# #         counter += 1
# #         start += 1


# while start < n-1:

#     if  (num_list[start] + num_list[end] < target) & (end != (len(num_list)-1)):
#         end += 1
#     elif num_list[start] + num_list[end] == target:
#         # counter += 1
#         # start += 1
#         # end -= 1
#         break
#     elif (num_list[start] + num_list[end] > target) or (end == (len(num_list)-1)):
#         start += 1
#         end = start + 1
# # print(start, end)
# try:

#     while True:
#         if (num_list[0] >= target) or (num_list[1] >= target):
#             break

#         if start == end:
#             break
#         else:
#             if num_list[start] + num_list[end] == target:

#                 counter += 1
#                 # print(counter)
#                 start += 1
#                 end -= 1
                
                
#                 if start > end: # 홀수개
#                     break
#                 elif (start+1 == end) & (num_list[start] + num_list[end] == target): # 짝수개여서 가운데에 안모이는 경우
#                     counter +=1
#                     break

#             elif num_list[start] + num_list[end] < target:
#                 start += 1
            
#             else:
#                 end -= 1
# except:
#     counter = 0
    
    

# print(counter)



# ver 5
# n = int(input())
# num_list = list(map(int, input().split()))

# num_list.sort()
# target = int(input())
# counter = 0

# max_idx = len(num_list)-1
# new_list =[]
# idx = 0
# while True:
#     if num_list[idx] >= target:
#         max_idx = idx

#     else: idx += 1

# new_list = num_list[:max_idx]
# s = len(new_list)//2
# e = len(new_list)//2 +1

# while True:

#     if s == 0 & e == max_idx:
#         break

#     if new_list[s] + new_list[e] >= target:
#         if s == 0 & e != max_idx:
#             e += 1
            
#         else:
#             s -= 1

#     elif new_list[s] + new_list[e] == target:
#         counter += 1
#         if 
#         s -= 1
#         e += 1

#     else:
#         if s != 0 & e == max_idx:
#             s -= 1
            
#         else:
#             e += 1
        

# 투포인터 이용
n = int(input())
num_list = list(map(int, input().split()))

num_list.sort()
target = int(input())
counter = 0
left = 0        # 왼쪽 포인터의 초기값 : 0
right = n-1     # 오른쪽 포인터의 초기값 : 1


while left < right:                                 # 맨왼쪽과 맨 오른쪽을 두 포인터의 끝과 끝으로 잡음
    tmp = num_list[left] + num_list[right]          # 포인터가 가리키는 수의 합을 임시로 담아 둠
    if tmp == target:                               # 목표값이랑 같을때 카운트
        counter += 1
    elif tmp < target:                                # 목표값보다 작을 때는 왼쪽 포인터를 우로 한칸이동
        left += 1
        continue
    right -= 1                                      # target보다 클때는 오른쪽 포인터를 좌로 한칸 이동
print(counter)
