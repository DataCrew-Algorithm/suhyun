import sys
input = sys.stdin.readline

N = int(input())

stairs = [int(input()) for _ in range(N)]

indices = [i for i in range(N)]

# 3개 연속되어 있는 것 제외하기

for i in range(2, N):
    stairs[i] += max(stairs[i-1], stairs[i-2])
print(stairs[-1])

# 그 동안 시행한 동적 계획법은 이전루트를 담고 있지 않으므로, 루트를 담는 코드를 짜야함

# 블로그 풀이
import sys
input = sys.stdin.readline

n = int(input())
stairs = [0] + [int(input()) for _ in range(n)] + [0] # index를 맞추기 위한 앞의 0, n이 1일때 점화식 index error를 해결하기 위한 뒤의 0
cache = [0] * (n+2)
cache[1] = stairs[1]            # 1층은 자기자신
cache[2] = cache[1] + stairs[2] # 2층은 1층+2층

for i in range(3, n+1): # 현재위치에 오기까지 두가지의 경우의 수 중 큰 값
                        # 두칸 전에서 +2 or (세칸 전에서 +2 & +1)
    cache[i] = max(cache[i-2], cache[i-3] + stairs[i-1]) + stairs[i]
print(cache[n])


