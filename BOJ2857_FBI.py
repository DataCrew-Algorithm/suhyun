name_list = []
ans_list = []

for _ in range(5):
    name = input()
    name_list.append(name)

for i in range(5):
    if 'FBI' in name_list[i]:
        ans_list.append(i+1)

if ans_list:
    print(*ans_list)

else: 
    print('HE GOT AWAY!')

    