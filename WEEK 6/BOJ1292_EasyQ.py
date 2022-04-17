A, B = map(int, input().split())

num_list = []

for i in range(1, 46):
    for _ in range(i):
        num_list.append(i)
# print(num_list[:10])
print(sum(num_list[A-1:B]))