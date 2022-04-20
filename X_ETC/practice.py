# # # print(len('abcdefghijklmnopqrstuvwxyz'))

# # # _list = [i for i in range(10)]
# # # print(_list)

# # list_of_tuple = [(i, j) for i in range(100) for j in range(100, 0, -1)]

# # list_of_tuple =[]
# # for i in range(10):
# #     for j in range(10, 0, -1):
# #         list_of_tuple.append((i, j))

# # print(list_of_tuple)


 
# # for ii in range(27, 0, -1):
# #     print(ii)


# # a, b = map(int, input().split())
# # print(type(a))

# # a = [i for i in range(-4, -2, 1)]
# # print(a)

# # c = [1,2,3]
# # d = c
# # print(id(c))
# # print(id(d))

# # a = [0]*3
# # # print(a)
# # print(id(a[0]))
# # print(id(a[1]))
# # print(id(a[2]))

# # a = [0] * 3
# # print(a)
# # print(id(a[0]))
# # print(id(a[1]))
# # print(id(a[2]))

# # my_list = [i for i in range(10)]
# # print(my_list)

# # count_dict2 = dict(zip(range(3), [0,0,0]))
# # print(count_dict2)

# # matrix = [[1,8,4], [3,5,7], [7,2,6]]
# # t = list(map(list, matrix))
# # print(t)
# # num_input = int(input())
# # ox_list = [input() for _ in range(num_input)]
# # print(ox_list)

# # lst = ['abc', 'bcd', 'edf']
# # lst = list(map(list, lst))
# # print(lst)
# # # print(lst[1][2])

# # pass_list = [list(map(int, input().split())) for i in range(4)]
# # print(pass_list)

# # for i in range(4):
# #     pass_list = list(map(int, input().split()))
# from copy import deepcopy
# import numpy as np
# # train_size = 50
# # batch_size = 100
# # batch_mask = np.random.choice(train_size, batch_size)

# # print(type(batch_mask))

# # a = np.array([0,1,2,3,4])
# # b = np.array([[5], [6], [7], [8], [9]])
# # c = b[a]
# # print(c)

# # a = [] *4
# # print(type(a))

# # a = []*4
# # print(a)

# # a.append(4)
# # print(a)

# # x = 'finr'
# # print(x[::-1])

# # x = input()
# # x_r = x[::-1]
# # x_r_int = int(x_r)

# # print(x_r_int)


# # str의 크기비교
# # print(str(3332) > str(32))


# # a = [0,1,2]
# # b = a[::-1]
# # print(b)

# # a = 1
# # b = 2
# # b = a

# # print(id(a))
# # print(id(b))

# # c = [1,2]
# # d = [1,2]
# # print(id(1))
# # print(id(1))
# # print(c==d)


# # mutable:list, dict, set - 객체 자체가 고윳값을 갖고 있음
# # immutable : int, float, tuple, str, bool - 문자 자체가 고유값을 가진놈

# # c, d는 id가 다름. 리스트라는 놈 자체가 id를 가짐


# # a = [1, 2, 3, [4,5], 6]
# # b = a
# # print(id(a))
# # print(id(b))

# # a[0] = 100
# # print(b)

# # a[3][0] = 400

# # print(b)

# # import copy
# # c = [1, 2, 3, [4,5], 6]
# # d = copy.deepcopy(c)

# # c[0] = 100
# # c[3][0] = 400
# # print(d)

# # aa = [0] * 3 # [0, 0, 0]
# # print(aa)

# # aa[0] = 1
# # print(aa) # [1,0, 0]

# # a = [ [0] * 3 ] * 3 # 하면 리스트안에 세개의 하위리스트가 아이디가 같아져버림
# # print(a) # [ [0,0,0], [0,0,0], [0,0,0] ]

# # a[1][1] = 100 # 
# # print(a)

# # mutable vs immutable

# # mutable: list, dict, set - 객체 자체가 고유 주소를 갖고 있음
# # ex ) list_a, list_b 아무리 내부 값이 다 같아도 주소가 다름. 복사해도 원래 리스트를 가리키는 거라, 원래 리스트가 변경되면 같이 변경

# # immutable : int, float, tuple, str, bool - 문자 자체가 고유값을 가진놈
# # ex ) 1, 2, 3 ... 자체의 주소가 배정되어 있음. 복사하면 그 주소를 가리키는 것 뿐임. 


# #  리스트라는 놈 자체가 id를 가짐

# # a = [0] * 3  은 int(immutable)인 0을 3개 복붙해서 리스트에 값이 들어간 것이므로 다른 것임(list를 복제하는게 아님!)

# # a = [1 ,2, 3]
# # print(enumerate(max(a)))

# # a = [1, 2, 3]
# # print(a.index(max(a)))

# # a = [1, 2, 3, 4, 4]
# # print(a.index(max(a)))

# a = []
# for j in range(3):
#     b = [i for i in range(3)]
#     a.append(b)

#     # for i in range(3):
#     #     a[j].append(i)
# # print(a)
# # print(id(a[0]), id(a[1]), id(a[2]))


# # a = [1,2,3,2,2]
# # print(a.count(2))

# # print(a.index(max(a)))

# def max_index(a, b, c):
#     if a ==  max(a, b, c):
#         if b == max(a, b, c):
#             if c == max(a, b, c):
#                 return 0, 1, 2
#             else: return 0, 1
#         elif c == max(a,b,c):
#             return 0, 2
#         return 0
#     elif b == max(a, b, c):
#         if c == max(a,b,c):
#             return 1, 2
#         return 1

#     else:
#         return 2 
        

# # print(list(max_index(100,200,200)))


# def elect_rule(score_1, score_2, score_3):
#     max_3 = list(max_index(score_1[2], score_2[2], score_3[2])) # 3의 갯수 최댓값의 인덱스 리스트
#     return max_3
#     # max_2 = list(max_index(score_1[1], score_2[1], score_3[1]))
#     # return max_2

# s1 = [1,4,1]
# s2 = [1,3,2]
# s3 = [4,1,1]


# print(elect_rule(s1,s2,s3))



# print(max([1]))

# a = [10,20,30,40,50]

# a = a[::-1]
# print(a)


# a = 'asdf'
# a[0] = a[0].upper()
# print(a)

# a = list('214212333')
# a.sort(reverse=1)
# print(a)

# import numpy as np

# a = np.array([1,2,3,4,5])
# b = np.array([0,2,3,4,5])
# c = np.array([2,3,4,5])

# print(np.where(a > b))
# print(np.where(b < a))
# print(type(np.where(a != c)[0][0]))




# a = ['abc', 'def']
# print(a[1].count('a'))
# a 

# print(5/2)

# l = [1,4,6]
# l


for i in range(0):
    print(i)