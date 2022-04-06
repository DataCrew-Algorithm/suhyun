# 선출 방식에 대한 정의
def elect_rule(max_l, each_sc):
    max_3 = max(each_sc[0].count(3), each_sc[1].count(3), each_sc[2].count(3)) # 3의 갯수의 최댓값
    list_max_3 = list(filter(lambda e:each_sc[e].count(3) == max_3, range(3))) # 3의 갯수 최댓값인 인덱스 리스트
    
    max_2 = max(each_sc[0].count(2), each_sc[1].count(2), each_sc[2].count(2)) # 2의 갯수의 최댓값
    list_max_2 = list(filter(lambda e:each_sc[e].count(2) == max_2, range(3))) # 2의 갯수 최댓값인 인덱스 리스트
    
    if len(max_l) == 3:
        if len(list_max_3) == 3:
            if len(list_max_2) >= 2:
                return 0

            else: return(list_max_2[0] + 1)

        elif len(list_max_3) == 2:
            if len(list_max_2) == 2:
                return 0
            
            else: return(list_max_2[0] + 1)

        
        else: return(list_max_3[0] + 1)

    elif len(max_l) == 2:
        if len(list_max_3) == 2:
            if len(list_max_2) == 2:
                return 0
            
            else: return(list_max_2[0] + 1)
        else: return(list_max_3[0] +1)

    else: return max_l[0][0] + 1  # 유일한 값을 호출


# max_list = [[0,13], [2,13]]
# each_score = [[3,2,3,1,3,1], [1,3,1,2,1,2], [2,1,2,3,2,3]]

max_list = [[0,12], [1,12], [2,12]]
each_score = [[1,3,2,1,3,2], [2,1,3,2,1,3], [3,2,1,3,2,1]]

print(elect_rule(max_list, each_score))