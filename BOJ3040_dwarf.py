# 36개를 직접 다 적음 9c7
num_array = [[0,1,2,3,4,5,6],
            [0,1,2,3,4,5,7],
            [0,1,2,3,4,5,8],
            [0,1,2,3,4,6,7],
            [0,1,2,3,4,6,8],
            [0,1,2,3,4,7,8],
            [0,1,2,3,5,6,7],
            [0,1,2,3,5,6,8],
            [0,1,2,3,5,7,8],
            [0,1,2,3,6,7,8],
            [0,1,2,4,5,6,7],
            [0,1,2,4,5,6,8],
            [0,1,2,4,5,7,8],
            [0,1,2,4,6,7,8],
            [0,1,2,5,6,7,8],
            [0,1,3,4,5,6,7],
            [0,1,3,4,5,6,8],
            [0,1,3,4,5,7,8],
            [0,1,3,4,6,7,8],
            [0,1,3,5,6,7,8],
            [0,1,4,5,6,7,8],
            [0,2,3,4,5,6,7],
            [0,2,3,4,5,6,8],
            [0,2,3,4,5,7,8],
            [0,2,3,4,6,7,8],
            [0,2,3,5,6,7,8],
            [0,2,4,5,6,7,8],
            [0,3,4,5,6,7,8],
            [1,2,3,4,5,6,7],
            [1,2,3,4,5,6,8],
            [1,2,3,4,5,7,8],
            [1,2,3,4,6,7,8],
            [1,2,3,5,6,7,8],
            [1,2,4,5,6,7,8],
            [1,3,4,5,6,7,8],
            [2,3,4,5,6,7,8]]

dwarf_list = []
selected_dwarf = []
sum_tmp = 0

for _ in range(9):                      # 숫자 입력해서 리스트에 저장
    dwarf_list.append(int(input()))

for i in range(len(num_array)):         # 36번 돌면서
    for num in range(7):                # 7개씩 뽑는 작업을 반복
        idx = num_array[i][num]         # i번째 행에 num열을 선택하면 그것이 dawrf_list에서 뽑을 인덱스 번호

        selected_dwarf.append(dwarf_list[idx])
    
    if sum(selected_dwarf) != 100:
        selected_dwarf = []            # 100이 아니면 리스트를 비워주는 작업을 함

    else:                              # 정답은 유일하다 했으므로 발견하면 break로 탈출
        break

for j in range(7):
    print(selected_dwarf[j])




# 9c7= 9c2

# 두명을 솎아내고 나머지를 출력 
# 이중 for문으로 구현해서, pop으로 제거 -> 동시에 두개를 제거할 수 없음.

# 전체 - 100 = 제외할 두명의 숫자의 합
# 전체-100- ㅇ = ㅁ

dwarf_list = []

for _ in range(9):
    dwarf_list.append(int(input()))

sum_all = sum(dwarf_list)   # 9개 숫자의 총합

# 리스트에서 제거할 2명을 찾는 과정
for i in range(8):
    for j in range(i+1, 9): # 리스트를 돌면서 ㅁ값이 있나 찾는 과정
        if (sum_all - 100 - dwarf_list[i]) == dwarf_list[j]:
            # dwarf_list.pop(i)-> 두개를 한꺼번에 제거해야 되서 pop 사용불가(하나지우면 리스트가 바뀜)
            # dwarf_list.pop(i)

            tmp1, tmp2 = dwarf_list[i], dwarf_list[j]   # 그래서 remove로 값을 지정해서 없애는 방식 사용
            dwarf_list.remove(tmp1)
            dwarf_list.remove(tmp2)
            
            break               # 문제에서 답은 한가지로 나온다고 했으므로 발견즉시 for문 탈출
    if len(dwarf_list) == 7:    # 2개가 제거 되었을때만 첫번째 for문 탈출하게 해야함
        break

for num in range(7):
    print(dwarf_list[num])






