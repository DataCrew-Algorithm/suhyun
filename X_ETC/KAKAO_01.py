def solution(survey, choices):
    survey_rev = ["TR", "FC", "MJ", "NA"] # 거꾸로 되어있는 형태
    attr = ["RT", "CF", "JM", "AN"]         # 제대로 되어있는 형태

    score = [(choices[i] - 4) for i in range(len(choices))] # 4를 일괄적으로 빼준다.
   

    ans_list =[]
    for j in range(len(survey)):
        if survey[j] in survey_rev:                         # 거꾸로 되어있으면
            tmp = ''.join(list(reversed(survey[j])))        # 유형의 문자를 뒤집어서 담아주고
            survey[j] = tmp
            score[j] = score[j] - score[j] * 2              # 숫자는 -를 붙여준다


    total_scores = [0] * 4              # 각 지표별 점수 총합을 담을 리스트

    for k in range(len(survey)):
        if survey[k] == 'RT':
            total_scores[0] += score[k]
        elif survey[k] == 'CF':
            total_scores[1] += score[k]
        elif survey[k] == 'JM':
            total_scores[2] += score[k]
        if survey[k] == 'AN':
            total_scores[3] += score[k]

    for num in range(4):
        if total_scores[num] > 0:               # 0보다 클때는 뒤에 있는 유형쪽
            ans_list.append(attr[num][1])
        if total_scores[num] <= 0:              # 0이거나 작을때는 앞에 있는 유형쪽
            ans_list.append(attr[num][0])

    
    answer = ''.join(ans_list)                  # 한줄로 출력위해 리스트를 문자열로 합쳐줌
    return answer


# survey = ["AN", "CF", "MJ", "RT", "NA"]
survey = ["TR", "RT", "TR"]
# choices = [5, 3, 2, 7, 5]
choices = [7, 1, 3]
print(solution(survey, choices))

# ["RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"]
        
