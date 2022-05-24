N = int(input())

def checker(str):
    counter = 0
    alpha_list = [str[0]]   # 첫 문자는 넣어둠
    
    for a in range(1, len(str)):
        if str[a] != str[a-1]:          # 직전의 문자와 달랐는데
            if str[a] in alpha_list:    # 리스트에 있으면
                counter -= 1            # counter에 1을 빼주고 즉시 종료
                break
            else:                       # 리스트에 없는 경우에는 추가해줌.
                alpha_list.append(str[a])

    return counter
            

ans = 0
for _ in range(N):
    ans += checker(input())

print(ans+N)    # 전체 문자의 개수에서 Checker에서 체크된 만큼 빼줌
