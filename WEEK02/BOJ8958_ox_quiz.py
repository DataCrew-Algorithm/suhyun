num_input = int(input())                            # for문으로 int(input())만큼 문자열을 입력받음

ox_list = [input() for _ in range(num_input)]       # 문자열을 받아서 리스트에 저장
ox_list = list(map(list, ox_list))                  # 리스트안에 있던 값이 str이어서 변경을 못해서 하위리스트로 만들어줌

sum = [0] * num_input


# O를 찾아 인덱스를 반환(.index), 그 인덱스를 이용하여 그 O를 *로 바꿈. & 1을 점수값에 넣고 sum에다가 더해줌
# 그리고 그다음 O를 인덱스로 찾고, 그 인덱스 -1이 'O' 이면, 그전꺼에다 +1을해서 sum에다가 더해줌

for ii in range(num_input): #ox_list의 ii번째 값에 대하여
    num_o = ox_list[ii].count('O') 
    score_ox = 0

    for _ in range(num_o): # o의 갯수만큼 아래 짓 반복
        
        idx = ox_list[ii].index('O')
    
        if idx == 0:
            ox_list[ii][idx] = '*' # 임시로 바꿈. 다음번에 안세어지게 하기 위해서
            
            score_ox = 1
            sum[ii] += score_ox

        elif idx >= 1:

            if ox_list[ii][idx-1] == '*': # 하나 전 값이 '*'이면
                score_ox += 1
                sum[ii] += score_ox

            else: # 하나 전 값이 '*'이 아니면
                score_ox = 1
                sum[ii] += score_ox

            ox_list[ii][idx] =  '*'


for i in range(num_input):
    print(sum[i])


