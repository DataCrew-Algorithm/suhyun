score = 0
mus = [int(input())for _ in range(10)]
for i in range(10): 
    score += mus[i]
    try:

        if score == 100:
            print(score)
            break 
        # 각 경우의 수로 구별했기 때문에 답이 나오면 for문 뒤에꺼 안봐도 되서, 효율성을 위해서 각각 break 걸었어요.
        elif score < 100 and (score + mus[i+1])>100: 
            if (abs(100 - score) < abs(100-(score + mus[i+1]))):
                print(score)
                break
            elif (abs(100 - score) > abs(100-(score + mus[i+1]))):
                print(score + mus[i+1])
                break
            elif (abs(100 - score) == abs(100-(score + mus[i+1]))):
                print(score + mus[i+1])
                break
    except: 
        # index error가 리스트의 마지막 값이 날때 나는거라, 이 때 그냥 그 값을 출력해버리면 됨.
        print(score)


