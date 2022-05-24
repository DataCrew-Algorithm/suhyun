K = int(input())

nums = []
for _ in range(K):
    tmp = int(input())
    if tmp != 0:            # 나온 숫자를 스택에 추가
        nums.append(tmp)
    else:
        nums.pop()          # 0이 나오면, 스택에 제일 뒤를 꺼냄
print(sum(nums))


