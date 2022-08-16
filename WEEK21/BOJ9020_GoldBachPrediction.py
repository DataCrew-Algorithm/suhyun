import sys
input = sys.stdin.readline

T = int(input())
G = []  

for i in range(T):          # 입력받은 n을 차례대로 담아줌
    G.append(int(input()))

PN = [True] * (max(G)+1)    # 에라스토스테네스의 체를 구현하기 위한 초기화. n값중 최댓값 이하에 있는 소수를 다 찾기위한 max

PN[0], PN[1] = False, False

for i in range(2, int(max(G) ** 0.5) + 1): # 시간 단축하기 위해 제곱근 사용
    if PN[i] == True: # i가 소수인 경우
        j = 2
        while i * j <= max(G):
            PN[i * j] = False           # i를 제외한 i의 모든 배수 지우기
            j += 1

primeNums = []                          # max(G)이하의 수 중에서 소수를 다 여기에 담는다.
for i, v in enumerate(PN):
    if v:
        primeNums.append(i)

# print(primeNums)

for t in G:
    ans = []
    for num in primeNums:
        if ((t - num) in primeNums) & (num <= t - num): # 주어진 수 - 소수 = 소수 이고 & 앞의 수가 뒤의 수보다 작을때
            ans.append([num, t - num]) # [소수, 주어진 수 - 소수]를 리스트에 담음
    # print(ans)
    print(*max(ans))    # 이중 리스트의 max는 앞의 값을 기준으로 max하므로 

# # 블로그 풀이
# import sys
# input= sys.stdin.readline
# T = int(input().rstrip())
# # 10000보다 작은 prime number를 구하면 되겟네. => Prime Number를 직접 구하면, 합을 구하는 과정에서 좀 번거롭다.

# def Is_Prime(N):                    # 소수인지 판별하는 함수, 판별만 할때는 에라토스테네스의 체보다 그냥 구현하는게 낫다.
#     if N<2:                             # 그냥 나누어떨어지는 지로 판별하는게 낫다는 뜻
#         return False
#     for i in range(2, int(N**0.5)+1):
#         if N % i == 0:
#             return False
#     return True 

# while T:
#     target = int(input().rstrip())
#     A = target//2
#     B = target//2
#     # 투포인터로 양쪽으로 이동하는 방식
#     for i in range(target//2):
#         if Is_Prime(A) and Is_Prime(B): # 둘다 소수일때 멈추면 됨.
#             print(A,B)
#             break
#         else:
#             A -= 1
#             B += 1
#     T -= 1  # T의 횟수만큼 다 돌면(즉, T가 0이되면) 멈추게 하기 위해 -1씩 해줌
