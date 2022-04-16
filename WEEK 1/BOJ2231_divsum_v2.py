# 엑셀 파일에서 초록색 음영 칠한 부분을 찾는 방법
# 자리수의 갯수 * 9가 각 자리수합인 i의 최댓값임 

N = input()
N_int = int(N)

num_digit = len(N) # 몇 자리 수인지 알기
rept = num_digit * 9 # 자리수 * 9로 반복시행할 수를 구함
answer = 0

for i in range(rept, 0, -1): # 각 자리수의 합이 1 ~ (9 * num_digit)인 경우의수 
    #역순으로 돌리는 이유는 복수개일때 처음만나는 값이 최소값이 되게 만들기 위함임
    
    M = N_int - i # 시행착오로 구한 M의 값
    if M < 0:    # 역순으로 for문을 돌려서 M값이 -가 되는 경우가 발생하는 것을 배제
        continue
    sum_digit = sum(map(int, str(M)))
        
    if i == sum_digit: # 시행착오로 담아놨던 i와 이를 통해 구한 M의 각자리 수의 합이 같다면
        answer = N_int - i # 정답에 넣는다
        break # 각자리수 합이 최대인 값부터 돌렸으니 처음만났을때가 최솟값임.

print(answer)