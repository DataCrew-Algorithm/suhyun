
N = int(input())
# n을 구하려면 입력받은 값을 str로 변환한후 len으로 길이를 잰다.

num_digit = len(str(N)) # 몇자리의 수인지 알기 위해 문자열로 바꾸고 len
rept = num_digit * 9 # 자리수 * 9로 반복시행할 수를 구함
ans_list = [] # 최종적으로 정답값들의 min을 쓰기위해서

for i in range(1, rept+1): # 각 자리수의 합이 1 ~ (9 * num_digit)인 경우의수
    M = N - i # 시행착오로 구한 M의 값

    each_digit = [] # 각 자리숫자를 담을 리스트 초기화 - sum으로 합치기 위해

    # M의 각 자리숫자를 분해하는 작업
    for pwr in range(int(num_digit)-1, -1, -1): # 자릿수-1 의 역순출력
        M_each = int(M / 10 ** pwr) # 10의 pwr 제곱으로 나눈 몫을 원래 숫자에서 추출하여 
        each_digit.append(M_each) # list로 갖고 있는다. 
        M -= M_each * 10 ** pwr # 반복해서 맨 앞의 숫자를 떼냄(각 자리수 * 10^n)

    
    sum_digit = sum(each_digit) # 각 자리수의 합을 담는다.
        
    if i == sum_digit: # 시행착오로 담아놨던 i와 이를 통해 구한 M의 각자리 수의 합이 같다면
        ans_list.append(N-i) # 정답 리스트에 담는다 - 추후 최솟값 구하기 위해

if ans_list: # 리스트가 비어있지 않으면
    answer = min(ans_list) # 최솟값을 정답에
    print(answer)

else: print(0) # 그렇지 않으면, 0을 출력
