

num_list = [] # 피보나치 수열을 받을 리스트

n0 = 0
n1 = 1
n = int(input())

num_list.append(n0)
num_list.append(n1)


for i in range(n-1):    # 이미 n1은 채워져 있으므로 n-1개만 채우면 됨
    sum_tmp = num_list[i] + num_list[i+1] # 점화식
    num_list.append(sum_tmp)

print(num_list[n])
