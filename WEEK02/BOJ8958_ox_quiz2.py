# O를 찾아 인덱스를 반환(.index), 그 인덱스를 이용하여 그 O를 *로 바꿈. & 1을 점수값에 넣고 sum에다가 더해줌
# 그리고 그다음 O를 인덱스로 찾고, (그 인덱스 - 1)이 'O' 이면, 그전꺼에다 +1을해서 score에 그리고 그럴 sum에다가 더해줌

num_input = int(input())

ox_list = [input() for _ in range(num_input)]       #  for문으로 int(input())만큼 문자열을 입력 받아서 리스트에 저장

# 리스트안에 있던 값이 str이어서 문자열의 글자 하나하나 값 변경을 못하므로 리스트안에 하위리스트로 만들어줌
ox_list = list(map(list, ox_list))                  # 2차원 리스트

sum = [0] * num_input




for i in range(num_input):              # ox_list의 i번째 값에 대하여
    num_o = ox_list[i].count('O')       # 각 줄의 문자열에서 'O'의 갯수를 센다. 아래 for문 쓰려고.
    score_ox = 0

    for _ in range(num_o):              # 'O'의 갯수만큼 아래 짓 반복
        idx = ox_list[i].index('O')     # 'O'를 찾아서 그 인덱스를 넣음
    
        if idx == 0:                    # 0일때는 앞에 인덱스에 비교값이 없음
            ox_list[i][idx] = '*'       # 임시로 '*'로 바꿈. 다음번에 세어지면 안되기 때문.
            score_ox = 1                # 0번째 값의 점수는 무조건 1
            sum[i] += score_ox

        elif idx >= 1:                  # 하나 전 인덱스의 값과 비교함

            if ox_list[i][idx-1] == '*': # 하나 전 값이 '*'이면
                score_ox += 1
                sum[i] += score_ox

            else:                        # 하나 전 값이 '*'이 아니면
                score_ox = 1             # 점수는 다시 1부터 시작
                sum[i] += score_ox

            ox_list[i][idx] =  '*'       # 임시로 '*'로 바꿈. 다음번에 세어지면 안되기 때문.


for j in range(num_input):
    print(sum[j])


