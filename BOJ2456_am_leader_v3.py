# 세 인자를 비교해서, 최댓값의 인덱스를 호출하는 함수 정의
def max_index(a, b, c):
    if a ==  max(a, b, c):
        if b == max(a, b, c):
            if c == max(a, b, c):
                return [0, 1, 2]
            else: return [0, 1]
        elif c == max(a,b,c):
            return [0, 2]
        return [0]

    elif b == max(a, b, c):
        if c == max(a,b,c):
            return [1, 2]
        return [1]

    else:
        return [2] 

# 합의 최댓값 함수, 1번 후보자의 1,2,3점의 count, 2번후보자의 .., 3번후보자의 ..
def elect_rule(max_l, score_1, score_2, score_3):
 
    max_3 = list(max_index(score_1[2], score_2[2], score_3[2])) # 3의 갯수 최댓값의 인덱스 리스트
    max_2 = list(max_index(score_1[1], score_2[1], score_3[1])) # 2의 갯수 최댓값의 인덱스 리스트
    
    if len(max_l) == 3:                 # 최댓값 리스트에 3개 들어있다 = 최댓값이 3명이다
        if len(max_3) == 1:             # 3의 개수가 많은 사람이 유일할때
            return max_3[0] + 1         # 그 사람의 인덱스 + 1 (인덱스는 0부터 시작)

        else: return 0                  # 3의 개수가 많은 사람이 2명, 3명일 때는 그들의 점수구성이 같음


    elif len(max_l) == 2:               # 최댓값이 2명이다.
        if len(max_3) == 1:             # 3의 개수가 많은 사람이 유일할때,
            return max_3[0] + 1         # 그 사람의 인덱스 + 1
        
        else: return 0                  # 3의 개수가 많은 사람이 2명일때, 그들의 점수 구성이 같음

    else: return max_l[0][0] + 1        # 3의 개수 많은 사람이 유일할 때, 그 사람의 인덱스+1을 출력




    # if len(max_l) == 3:                       # 합이 3개가 같다. 그중에서,
    #     if len(max_3) == 3:                # 3의 개수 최대값이 3개 같은 것 중에서,
    #         if len(max_2) >= 2:                # 2의 개수 최대값이 3개나, 2개 같다 -> 0
    #             return 0

    #         else: return(max_2[0] + 1)         # 2의 개수가 최대값이 하나다.

    #     elif len(max_3) == 2:              # 3의 개수 최대값이 2개가 같다. 그중에서,
    #         if len(max_2) == 2:                # 2의 개수 최대값이 2개 같다. -> 0
    #             return 0
            
    #         else: return(max_2[0] + 1)         # 2의 개수가 최대값이 하나다.

        
    #     else: return(max_3[0] + 1)         # 3의 개수 최대값이 하나다.

    # elif len(max_l) == 2:                     # 합이 2개가 같다.
    #     if len(max_3) == 2:                # 3의 개수 최대값이 2개 같다. 그중에서,
    #         if len(max_2) == 2:                # 2의 개수 최대값이 2개 같다. -> 0
    #             return 0                            
            
    #         else: return(max_2[0] + 1)         # 2의 개수 최대값이 하나다.
    #     else: return(max_3[0] +1)          # 3의 개수 최대값이 하나다.
    
    # else: return max_l[0][0] + 1              # 합이 하나만 같다.



rept = int(input())
score_list1 = [0] * 3   #1번 후보자의 1,2,3점의 개수를 넣은 리스트
score_list2 = [0] * 3
score_list3 = [0] * 3

sum_cand1 = 0           # 1번 후보자의 총점
sum_cand2 = 0
sum_cand3 = 0

for _ in range(rept): # 입력받은 횟수만큼 점수를 입력받아서 리스트로 저장
    score1, score2, score3 = map(int, input().split())
    score_list1[score1-1] += 1  # 1점이면 0번에, 2점이면 1번에, 3점이면, 2번에
    score_list2[score2-1] += 1
    score_list3[score3-1] += 1

for i in range(3): 
    sum_cand1 += score_list1[i] * (i+1) # 1번 후보자의총점계산 0번인덱스(1점) * (0+1)점
    sum_cand2 += score_list2[i] * (i+1)
    sum_cand3 += score_list3[i] * (i+1)

max_list = [] # 최댓값의 [인덱스, 값]을 담을 리스트 [100, 300, 300]--> [[1, 300], [2, 300]]

sum_list = [sum_cand1, sum_cand2, sum_cand3]
for idx, val in enumerate(sum_list):    # 리스트의 인덱스와 값을 순차적으로 반환
    if val == max(sum_list):                  # 이 때, 최댓값을 발견하면
        max_list.append([idx, val])     # 인덱스, 값 순서의 리스트를 max_list에 저장

elect_idx = elect_rule(max_list, score_list1, score_list2, score_list3)
print(elect_idx, max_list[0][1])




