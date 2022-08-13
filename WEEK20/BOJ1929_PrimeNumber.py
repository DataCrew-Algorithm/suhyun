# 시간초과
import sys

input = sys.stdin.readline

M, N = map(int, input().split())

for i in range(M, N+1):
    for j in range(2, i):   # i보다 작은수인 j로 나누어 떨어지면 소수가 아니다
        if i % j == 0:      # 나누어 떨어진다. = 소수가 아니다.
            break           # 그 즉시 해당 숫자는 소수가 아니므로 탈락
    else:
        print(i)

# 블로그 힌트 -> i의 제곱근까지만 하면 됨
# 시간 너무 오래걸림 5708ms -> 에라스토스의 체로 구하는게 빠름
import sys

input = sys.stdin.readline

M, N = map(int, input().split())

for i in range(M, N+1):
    if i == 1:  # M이 1부터 시작하므로 1일때는 안 돌아야함
        continue
    else:                   # 제곱근 까지만 구하면 됨(제곱했을 때 수 까지만 나오면 그 위는 고려할 필요가 없음)
        for j in range(2, int(i**0.5)+1):   
            if i % j == 0:      # 나누어 떨어진다. = 소수가 아니다.
                break
        else:
            print(i)

# 에라스토스의 체를 이용한 풀이
# 2부터 소수에 어떤 수를 곱한것은 소수가 아니다라는 성질을 이용하여 차례대로 False로 바꿔가며 제거해 나아가는 방식
def erastosSieve(end): # 시작, 끝 범위 수 입력 (0 ~ n까지)
    erastos = [True] * (end + 1) # 소수 판별 여부를 담는 리스트
    erastos[0], erastos[1] = False, False # 0과 1은 소수가 아니므로 False로 초기화
    
    for i in range(2, int(end ** 0.5) + 1): # 시간 단축하기 위해 제곱근 사용
        if erastos[i] == True: # i가 소수인 경우
            j = 2
            while i * j <= end:
                erastos[i * j] = False # i를 제외한 i의 모든 배수 지우기
                j += 1
                
    return erastos

start, end = map(int, input().split())

for i, v in enumerate(erastosSieve(end)):
    if i>= start and v:
        print(i)
