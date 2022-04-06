name_list = []   # 입력을 받을 리스트
ans_list = []    # FBI 요원의 번호를 받을 리스트

for _ in range(5):
    name = input()
    name_list.append(name)

for i in range(5):
    if 'FBI' in name_list[i]:   # 'FBI'라는 문자가 각 요원 번호에 포함되어 있으면,
        ans_list.append(i+1)    # 인덱스에 + 1한 것을 리스트에 담는다.

if ans_list:
    print(*ans_list)            # 리스트에서 벗어나기

else: 
    print('HE GOT AWAY!')

    