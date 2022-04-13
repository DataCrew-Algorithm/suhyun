# 각 줄을 돌면서 X표시 된곳의 인덱스를 담음. 다만, 원래 있으면 안담음
N, M = map(int, input().split())    # 행과 열의 개수를 담음
guard_list = []                     # 성의 상태를 담음
guard_idx = []                      # 경비원의 인덱스를 담음(적어도 한명이라도 있는 열의 index)
blank_guard = 0

for _ in range(N):                  # 성의 상태를 담음
    guard_list.append(input())
# print(guard_list)

for j in range(N):                      # 1st) 각 행을 돌면서 가드가 없는 행을 찾는다.
    if guard_list[j].find('X') == -1:   # 각 행에 경비원이 한명도 없는 경우가 생기면 필요 가드 수에 +1 해줌
        blank_guard += 1                # 아무리 모든 열이 차있어도 하나를 배치해줘야 하기 때문.
# print(blank_guard)
for i in range(N):                      # 2nd) 각 행에서 경비원이 있는 곳의 인덱스를 반환, 
    count = guard_list[i].count('X')    # 각 행의 몇명의 가드가 있는지 센다.
    for _ in range(count):              # 그 수 만큼 'X'의 인덱스를 찾아서 반환하기 위해서
        try:                            # 해당 열에 한명도 없는 경우 고려하기 위해 try, except 사용
            idx = guard_list[i].index('X')
            
            guard_list[i] = guard_list[i].replace('X', '*', 1)  # 한 번 인덱스를 저장한 가드를 또 세면 안돼서 *로 바꿔줌 
            # print(guard_list)
            if idx not in guard_idx:    # 이미 그 열에 다른 가드가 있으면 인덱스 추가하지 않음.
                guard_idx.append(idx)
        except:
            pass                        # index함수를 쓰므로, 찾는 값이 없을 때 error가 나면 넘기게 하기 위함.
# print(guard_idx)


print(max(M - len(guard_idx), blank_guard)) 
# 열의 수인 M만큼은 필요함. 그래서 M에서 현재 각 열에 채워진 인원에 부족한 만큼 필요
# 또한, 적어도 빈 열만큼은 채워져야 하므로 max와 빈 열의 수를 쓰는 것임.