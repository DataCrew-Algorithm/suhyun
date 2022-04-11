# 오름차순으로 정렬을 하고, 순차적으로 두개씩 비교해서 둘의 차이가 1이 아닐때에는,
# 그 사이 값이 빈 번호임.

num_list = [int(input()) for _ in range(28)]    # 28개 출석번호를 담을 리스트
ans_list = []

num_list.sort()     # 오름차순 정렬

# 맨앞에 1,2가 없거나 뒤에 29 30인 경우에 문제가 발생.
for i in range(27):     # 2개씩 비교하니 하나 전까지 하면 됨
    if num_list[i+1] - num_list[i] > 1:
        ans_list.append(num_list[i]+1)

        if len(ans_list) == 2:
            break
        
        
if len(ans_list) == 1:
    ans_list.append(30)

elif len(ans_list) == 0:
    ans_list.append(29)
    ans_list.append(30)

    
print(ans_list[0])
print(ans_list[1])

# 하나씩 있나 없나 확인.

num_list = [int(input()) for _ in range(28)]    # 28개 출선번호를 담을 리스트
ans_list = []

num_list.sort()     # 오름차순 정렬

for i in range(1, 31):              # 1~30까지 있나 하나씩 확인        
    if i not in num_list:           # 그 번호가 리스트 안에 없으면
        ans_list.append(i)          # 정답리스트에 넣어주기

print(ans_list[0])
print(ans_list[1])