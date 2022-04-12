# 각 줄을 돌면서 X표시 된곳의 인덱스를 담음. 다만, 원래 있으면 안담음
N, M = map(int, input().split())
guard_list = []
guard_idx = []
blank_guard = 0

for _ in range(N):
    guard_list.append(input())
# print(guard_list)

for j in range(N):
    if guard_list[j].find('X') == -1:
        blank_guard +=1
# print(blank_guard)
for i in range(N):
    count = guard_list[i].count('X')
    for _ in range(count):
        try:
            idx = guard_list[i].index('X')
            
            guard_list[i] = guard_list[i].replace('X', '*', 1)
            # print(guard_list)
            if idx not in guard_idx:
                guard_idx.append(idx)
        except:
            pass
# print(guard_idx)

# if len(guard_idx) == 0:
#     print(blank_guard)

# else:
print(max(M - len(guard_idx), blank_guard))