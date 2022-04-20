# B-> A, A->B로 바꾸려고 하였고
# 그 과정에서 겹치지 않게 하기 위해서 *, # 등 임시 기호로 바꿔주려 하였으나 메모리초과 
# 동시에 바꿔주는 방법 없을까 생각

# K = int(input())

# char = "A"
# for _ in range(K):
#     char = char.replace('B', '*')
#     char = char.replace('A', '#')
#     char = char.replace('*', 'BA')
#     char = char.replace('#', 'B')

# A = char.count('A')
# B = char.count('B')

# print(A, B)



# ver.2
# 리스트에
# K = int(input())

# char = list("A") # 초기값인 A를 담는다.



# while True:
#     try:  # index함수는 찾는 값이 없을 때 에러이므로
#         idx = char.index('A')         
#         char[idx] = "*"
#         idx_tmp = char.index('*')
#         char[idx_tmp] = "B"

#         idx2 = char.index('B')
#         char[idx2] = "#"
#         char = str(char.replace("#", 'BA'))

#     except:   #index함수 에러나면 
#         break
# print(char)

# A = char.count('A')
# B = char.count('B')

# print(A, B)


# ver.3 # 피보나치 수열
K = int(input())

A_list = [1, 0]
B_list = [0, 1]

for i in range(K-1):
    A = A_list[i] + A_list[i+1]
    B = B_list[i] + B_list[i+1]
    A_list.append(A)
    B_list.append(B)

print(A_list[K], B_list[K])



