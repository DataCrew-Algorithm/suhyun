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
# K = int(input())

# char = list("A")


# while True:
#     try:
#         idx = char.index('A')
#         char[idx] = "*"
#         idx_tmp = char.index('*')
#         idx2 = char.index('B')
#         char[idx2] = "#"
#         idx_tmp = char.index('*')

#         char[idx_tmp] = "B"
#         char = str(char.replace("*", 'BA'))
#     except:
#         break
# print(char)

# A = char.count('A')
# B = char.count('B')

# print(A, B)


# ver.3
K = int(input())

A_list = [1, 0]
B_list = [0, 1]

for i in range(K-1):
    A = A_list[i] + A_list[i+1]
    B = B_list[i] + B_list[i+1]
    A_list.append(A)
    B_list.append(B)

print(A_list[K], B_list[K])



