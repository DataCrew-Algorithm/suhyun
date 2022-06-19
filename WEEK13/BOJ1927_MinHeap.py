import heapq
import sys

nums = []
N = int(input())
for _ in range(N):
    tmp = int(sys.stdin.readline())
    if nums:    # heap 안에 숫자가 있을때,
        if tmp == 0:
            print(heapq.heappop(nums))

        else:
            heapq.heappush(nums, tmp)
    
    else:       # heap이 비어있을 때,
        if tmp == 0:
            print(0)
        else:
            heapq.heappush(nums, tmp)