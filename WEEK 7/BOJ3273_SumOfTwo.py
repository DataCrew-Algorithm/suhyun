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

# ver2


n = int(input())
counter = 0

num_list = list(map(int, input().split()))
target = int(input())
i = 0
num_list.sort()

new_list = []

# if target < num_list[0]:
#     print(0)
# else:
while True:
    if num_list[i] >= target or i == n-1:
        break    
    else: 
        i += 1
        # print(i)
new_list = num_list[:i+1]
# print(new_list)
# for i in range(len(new_list)-1):
#     for j in range(i+1, len(new_list)):
#         if new_list[i] + new_list[j] == target:
#             counter += 1

# ???if target >= new_list[0]:
#     if n == 2 & sum(new_list) == target:
#             print(1)


if sum(new_list[-2:]) <= target:
    print(0)

else:
    for i in range(round((len(new_list)/2)+0.1)):
        for j in range(i+1, len(new_list)):
            if (target - new_list[i]) == new_list[j]:
                counter += 1
                break
                

    if ((target / 2) in new_list) & n >= 2:
        counter -= 1


    print(counter)


# 7 8 9 10 11 12-> target 5일 때, 문제 발생 해결

    