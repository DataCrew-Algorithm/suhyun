import sys
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())

def dfs(v):
    for i in range(N):
        if (tmp[i] == 0) & (graph[v][i] == 'Y'):
            tmp[i] = 1
            dfs(i)


# graph = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
graph = [sys.stdin.readline().rstrip() for _ in range(N)]
# print(graph)
result = []
for x in range(N):
    cnt = 0
    tmp = [0] * N
    dfs(x)
    print(tmp)
    result.append(sum(tmp))
print(result)

if max(result) == 0:
    print(0)
else:
    print(max(result)-1)

# 친구의 친구 까지만 가능하고 그 이상은 불가능하므로 답이 틀림.

# 블로그 풀이 참고 - 플루이드 워셜 -> 추가 학습 필요
N = int(input())
graph = [list(input()) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] == 'Y'):
                visited[i][j] = 1

result = 0
for visit in visited:
    result = max(result, sum(visit))
print(result)



