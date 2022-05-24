N = int(input())
num_list = []

for _ in range(N):
    num_list.append(int(input()))

num_list.sort() # 오름차순으로 정렬

for ans in num_list:
    print(ans)