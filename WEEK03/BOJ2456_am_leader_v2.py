# 2차원 리스트를 만들어서 세로읽기 진행

# 선출 방식에 대한 정의
def elect_rule(max_l, each_sc):
    max_3 = max(each_sc[0].count(3), each_sc[1].count(3), each_sc[2].count(3)) # 3의 갯수의 최댓값
    list_max_3 = list(filter(lambda e:each_sc[e].count(3) == max_3, range(3))) # 3의 갯수 최댓값인 인덱스 리스트
    
    max_2 = max(each_sc[0].count(2), each_sc[1].count(2), each_sc[2].count(2)) # 2의 갯수의 최댓값
    list_max_2 = list(filter(lambda e:each_sc[e].count(2) == max_2, range(3))) # 2의 갯수 최댓값인 인덱스 리스트
    
    if len(max_l) == 3:                       # 합이 3개가 같다. 그중에서,
        if len(list_max_3) == 3:                # 3의 개수 최대값이 3개 같은 것 중에서,
            if len(list_max_2) >= 2:                # 2의 개수 최대값이 3개나, 2개 같다 -> 0
                return 0

            else: return(list_max_2[0] + 1)         # 2의 개수가 최대값이 하나다.

        elif len(list_max_3) == 2:              # 3의 개수 최대값이 2개가 같다. 그중에서,
            if len(list_max_2) == 2:                # 2의 개수 최대값이 2개 같다. -> 0
                return 0
            
            else: return(list_max_2[0] + 1)         # 2의 개수가 최대값이 하나다.

        
        else: return(list_max_3[0] + 1)         # 3의 개수 최대값이 하나다.

    elif len(max_l) == 2:                     # 합이 2개가 같다.
        if len(list_max_3) == 2:                # 3의 개수 최대값이 2개 같다. 그중에서,
            if len(list_max_2) == 2:                # 2의 개수 최대값이 2개 같다. -> 0
                return 0                            
            
            else: return(list_max_2[0] + 1)         # 2의 개수 최대값이 하나다.
        else: return(list_max_3[0] +1)          # 3의 개수 최대값이 하나다.
    
    else: return max_l[0][0] + 1              # 합이 하나만 같다.
        
        


rept = int(input())
score_list = [] # 입력받은 점수의 리스트를 담을 리스트 (2차원 리스트)
each_score = [] # 각 후보자마다 점수를 담을 리스트 (2차원 리스트 - 세로읽기해서)

for _ in range(rept): # 입력받은 횟수만큼 점수를 입력받아서 리스트로 저장
    score_list.append(list(map(int, input().split())))

for col in range(3):
    # for rows in range(rept):
    tmp = [score_list[rows][col] for rows in range(rept)] # 세로읽기를 통해 각 후보자의 점수를 리스트에 담음
    each_score.append(tmp)                                # 그 리스트를 each_score 리스트에 담음(2차원 리스트)

        # tmp.append[col](score_list[rows][col])

        # sum_list[col] += score_list[rows][col]
sum_list = [sum(each_score[num]) for num in range(3)]     # 각 후보자의 점수 각각을 담은 하위 리스트별 점수 합계를 구함

elected = max(sum_list) # 최댓값을 구해놓기
max_list = []


for idx, val in enumerate(sum_list):    # 리스트의 인덱스와 값을 순차적으로 반환
    if val == elected:                  # 이 때, 최댓값을 발견하면
        max_list.append([idx, val])     # 인덱스, 값 순서의 리스트를 max_list에 저장

# print(max_list)

ans_index = elect_rule(max_list, each_score)

print(ans_index, elected)
