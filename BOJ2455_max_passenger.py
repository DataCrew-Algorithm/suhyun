pass_list = [list(map(int, input().split())) for i in range(4)]
# 각 정거장에 해당하는 4줄을 입력받아서 리스트에 담는다.(스플릿으로 빈칸을 기준으로 두개씩 입력)
# 이중리스트를 만들었음. 두개씩 리스트에 담고, 큰리스트에 담는.

pass_stn = [] # 각 정거장별 승객의 합 리스트
sum_pass = 0

for num in range(4): # 4개의 역을 돌면서 
    sum_pass = sum_pass - pass_list[num][0] + pass_list[num][1] # 누적해서 더해놓으면서
    pass_stn.append(sum_pass) # 그때 그때 각 정거장 리스트에 추가

print(max(pass_stn))



# for i in range(4):
#     pass_list = list(map(int, input().split()))