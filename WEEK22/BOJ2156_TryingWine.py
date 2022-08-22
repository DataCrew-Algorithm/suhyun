import sys
input = sys.stdin.readline

n = int(input())

wine = [0] + [int(input()) for _ in range(n)] + [0] # 인덱스와 포도주 번호 맞추기 위한 0, n이 1일때를 위한 0

cache = [0] * (n+2)

cache[1] = wine[1]
cache[2] = cache[1] + wine[2]

for i in range(3, n+1): # 현재 시점에서 안먹는 경우가 있다는 것이 포인트 (계단은 그 자리에 오면 숫자를 더해야하지만, 포도주는 아님)
    cache[i] = max(cache[i-1], max(cache[i-2], cache[i-3] + wine[i-1]) + wine[i])

print(max(cache))
print(cache)
