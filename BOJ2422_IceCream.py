N, M = map(int, input().split())
num_list = []
comb_list = []

for i in range(1, N+1):
    num_list.append(i)

for _ in range(M):
    tmp = list(map(int, input().split()))
    comb_list.append(tmp)

for j in range(M):
    comp_list = num_list.remove(comb_list[j][0])
    comp_list = num_list.remove(comb_list[j][1])


