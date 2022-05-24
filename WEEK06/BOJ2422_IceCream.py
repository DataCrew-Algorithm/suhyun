# ver.1
# N, M = map(int, input().split())
# num_list = []
# comb_list = []

# for i in range(1, N+1):
#     num_list.append(i)

# for _ in range(M):
#     tmp = list(map(int, input().split()))
#     comb_list.append(tmp)

# for j in range(M):       
#     comp_list = num_list.remove(comb_list[j][0])
#     comp_list = num_list.remove(comb_list[j][1])




# # ver2. 전체 조합을 다 구하고, 부분집합인 경우만 빼주는 방식
# bad_flavor = []
# comb_list = []      # 모든 조합을 담을 리스트
# ans_set = []        # 중복되면 안되니까 집합으로

# N, M = map(int, input().split())
# for _ in range(M):
#     tmp = list(map(int, input().split()))
#     bad_flavor.append(tmp)
    
# ice_list = [i+1 for i in range(N)] # 아이스크림 전체


# for j in ice_list:
#     for k in range(j+1, len(ice_list)+1):
#         for l in range(k+1, len(ice_list)+1):
#             tmp_list = []
#             tmp_list.append(j)
#             tmp_list.append(k)
#             tmp_list.append(l)
#             comb_list.append(tmp_list)
# # print(bad_flavor)
# # print(comb_list)
# for b in range(len(bad_flavor)):
#     for c in range(len(comb_list)):

#         # print(set(bad_flavor[b]))
#         # print(set(comb_list[c]))
#         # 전체 조합에서 한개씩 꺼내서 bad_flavor가 부분집합인 경우에만 추가.
#         if set(bad_flavor[b]) == set(bad_flavor[b]).intersection(set(comb_list[c])):
#             if comb_list[c] not in ans_set:
#                 ans_set.append(comb_list[c])

# # print(ans_set)
# print(len(comb_list) - len(ans_set))


# ver3 : 전체 개수만 구하고, 안되는 애들 집합을 따로구해서 그 갯수 빼기
ans_list = []

N, M = map(int, input().split())
for _ in range(M):
    tmp = list(map(int, input().split()))
    # print(tmp)
    for j in range(1, N+1):         # 1, 2-> 3, 4, 5를 추가해서 
        if j not in tmp:
            ans = tmp + [j]
            if set(ans) not in ans_list:    # 중복된게 들어가 있으면 안되니까 set으로 해주고
                ans_list.append(set(ans))   # 안들어가 있을 때만 추가


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
    


# def factorial(n):
#     ans = 1
#     for i in range(1, n+1):
#         ans *= i

#     return ans

# l = []
# for i in range(N):
#     l.append(i)

count_all = int(factorial(N) / (factorial(M) * factorial(N-M)))



print(count_all - len(ans_list))

# ver 4
# N, M = map(int, input().split())

# bad_list =[]
# comb_list = []
# for _ in range(M):
#     tmp = list(map(int, input().split()))
#     bad_list.append(set(tmp))
# print(bad_list)

# if N == 1 or N == 2:
#     pass

# for n1 in range(1, N-1):
#     for n2 in range(n1+1, N):
#         for n3 in range(n2+1, N+1):
#             comb_set = set([n1, n2, n3])
#             for i in range(M):
#                 if bad_list[i] != bad_list[i].intersection(comb_set):
#                     if comb_set not in comb_list:
#                         comb_list.append(comb_set)

# print(comb_list)




