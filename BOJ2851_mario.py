# 누적합의 경우의 수의 합과 100의 차이가 최소가 되었을 때 출력

score_list = [int(input()) for _ in range(10)] # 입력받아서
sum_list = []                                   # 각 누적합을 넣음.

for i in range(10):                             # 총 10가지 경우의 수
    tmp = abs(100 - sum(score_list[0:i+1]))     # 100과의 차이의 최솟값
    sum_list.append(tmp)                        # 그 차이를 리스트에 담아서
    

                                                # 그 차이의 최솟값을 출력
print(min(sum_list)+100)                        # 100이 빠진 차이값이니 100을 더함



# 누적합의 경우의 수의 합과 100의 차이가 최소가 되었을 때 출력

score_list = [int(input()) for _ in range(10)] # 버섯 갯수 10개 입력받아서 리스트에 넣음
sum_list = []       # 각 경우의 누적합들을 담은 리스트
abs_list = []       # 100 과의 차이의 절댓값을 씌운 것의 리스트
comp_list = []      # 차이의 최소값이 복수개 일때 비교하기 위한 리스트

for i in range(10):                     # 누적합은 총 10개의 경우의 수가 있음
    tmp1 = sum(score_list[0:i+1])       # 각 경우의 합
    sum_list.append(tmp1)

    tmp2 = abs(100 -sum_list[i])        # 그 합을 100에서 뺐을 때의 차이
    abs_list.append(tmp2)

    
for j in range(10):                     # 100과의 차이가 최소가 되는 값이 복수개 일 경우에 
    if abs_list[j] == min(abs_list):
        comp_list.append(sum_list[j])   # 그에 해당하는 누적합을 리스트에 담음

try:
    print(max(comp_list))               # 둘 중 누적합이 큰 것이 답임
except:                                 # 리스트에 한개만 있으면 max를 못쓰니까 except
    print(comp_list)                    # 그 한개를 그대로 출력

    


# print(min(sum_list)+100)