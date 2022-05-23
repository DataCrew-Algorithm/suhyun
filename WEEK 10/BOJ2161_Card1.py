from collections import deque

N = int(input())        # queue = [1, 2, 3, 4, 5, 6, 7]
nums = deque([i+1 for i in range(N)]) # 1~N까지를 큐로 만듦

while len(nums) != 1:               # 한 개 남을 때 까지 반복
    print(nums.popleft(), end=' ')  # 제일 위(맨 왼쪽)버리면서 출력
    tmp = nums.popleft()            # 제일 밑(맨 오른쪽)으로 넣음
    nums.append(tmp)

print(nums[0])

