# ver1. deque를 이용한 풀이 -> 시간초과 (4%)
import sys
from collections import deque
read = sys.stdin.readline

N, d, k, c = map(int, read().split())


nums = deque([]) # rotate를 위해서 deque를 씀
for _ in range(N):
    nums.append(int(read()))

len_list = []   
for _ in range(N):
    tmp = deque([])                 
    for i in range(k):              # 앞에서부터 k개의 초밥번호를 tmp에 담음
        tmp.append(nums[i])
    tmp.append(c)                   # 쿠폰에 나온 것을 담음
    len_list.append(len(set(tmp))) # tmp를 set으로 바꾼 것에 몇개가 있는지를 추가
    nums.rotate(1)

print(max(len_list))


# ver2


import sys
from collections import deque
read = sys.stdin.readline

N, d, k, c = map(int, read().split())


nums = deque([])
for _ in range(N):
    nums.append(int(read()))

len_list = []
for _ in range(N):
    tmp = set()
    for i in range(k):
        tmp.add(nums[i])
    if c not in tmp:                  # not in으로 바꿔서 안들어 있을때만 +1해줌
        len_list.append(len(tmp)+1)
    else:
        len_list.append(len(tmp))
    nums.rotate(1)

print(max(len_list))


# ver3
import sys
read = sys.stdin.readline

N, d, k, c = map(int, read().split())

nums = []   # 리스트로 해봄
for _ in range(N):
    nums.append(int(read()))

left = 0
result = []
for _ in range(N):
    eaten = [0] * (d+1) # 1 ~ d+1 의 스시 번호에 안먹었으면 0, 먹었으면 1

    for i in range(k):
        idx = left % N      # N으로 나눈 나머지를 idx로
        if eaten[nums[idx]] == 0:
            eaten[nums[idx]] = 1    # 0일때는 먹은것이니 1로 바꿔줌. 이미 먹은것인 1은 그대로 둠
        left += 1
    
    cnt = 0
    for ss in eaten:    # eaten 리스트에서 ss의 개수만 세서 cnt로 표시
        if ss == 1:
            cnt += 1
    
    if eaten[c] == 0:   # 쿠폰에서 나온 번호를 안먹었으면 +1
        cnt += 1
    
    result.append(cnt)

print(max(result))
    
    
# # ver4 블로그풀이 ?? 실패
# import sys

# n, d, k, c = map(int, sys.stdin.readline().rsplit())
# arr = [int(sys.stdin.readline()) for _ in range(n)]
# lp, rp = 0, 0
# answer = 0

# while lp != n:
#     rp = lp + k
#     case = set()
#     addable = True
#     for i in range(lp, rp):
#         i %= n
#         case.add(arr[i])
#         if arr[i] == c: 
#             addable = False

#     cnt = len(case)
#     if addable: 
#         cnt += 1
#     answer = max(answer, cnt)
#     lp += 1

# print(answer)


# ver5 블로그풀이 defaultdict 이용한 투포인터
import sys
from collections import defaultdict

n, d, k, c = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.extend(arr)   # 원형이라서 2개를 이어준다. !!중요한 아이디어
left = 0
right = 0
dict_ = defaultdict(int)
result = 0

dict_[c] += 1          # 보너스는 무조건 먹기 

# 1. 처음에 k 구간만큼 먹기
while right < k:
    dict_[arr[right]] += 1
    right += 1

# 2. 슬라이딩 윈도우 적용 
while right < len(arr):
    result = max(result, len(dict_))
    # 1. 맨 왼쪽 초밥 제거
    dict_[arr[left]] -= 1
    if dict_[arr[left]] == 0:  # 삭제된 왼쪽 초밥이 0 이면 dict 삭제 
        del dict_[arr[left]]
    # 2. 오른쪽 초밥 추가하기 
    dict_[arr[right]] += 1
    # 왼쪽 위치 + 1
    left += 1
    # 오른쪽 위치 + 1
    right += 1

print(result)








