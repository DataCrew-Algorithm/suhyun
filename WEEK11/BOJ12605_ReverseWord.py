# ver1. 슬라이싱을 이용한 풀이 64ms

N = int(input())

for i in range(N):
    tmp = input().split(' ') # 공백을 기준으로 나눠서 리스트로
    print(f'Case #{i+1}: {" ".join(tmp[::-1])}') # 그걸 뒤집어서 출력


# ver2. 스택을 이용한 풀이 64ms
N = int(input())

for i in range(N):
    ans = []
    tmp_list = input().split(' ')
    while tmp_list != []:
        tmp = tmp_list.pop()
        ans.append(tmp)
    ans = ' '.join(ans)
    print(f'Case #{i+1}: {ans}')
