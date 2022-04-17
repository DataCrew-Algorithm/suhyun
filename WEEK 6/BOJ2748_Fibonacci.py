

num_list = []


n0 = 0
n1 = 1
n = int(input())

num_list.append(n0)
num_list.append(n1)

if n == 0 or n == 1:
    print(num_list[n])

else:
    for i in range(n-1):
        sum_tmp = num_list[i] + num_list[i+1]
        num_list.append(sum_tmp)
        # print(num_list)

    print(num_list[n])
