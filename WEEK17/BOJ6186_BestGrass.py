# 배추 문제와 같음
import sys
sys.setrecursionlimit(1000000)

R, C = map(int, sys.stdin.readline().split())

graph = []
for i in range(R):
    tmp = list(sys.stdin.readline().rstrip())
    graph.append(tmp)


def dfs(x, y):
    global cnt
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < C) & (0 <= ny < R):
            if graph[ny][nx] == '#':
                # cnt += 1
                graph[ny][nx] = 'G'
                dfs(nx, ny)


# cnt = 0
# dfs(0, 0)
# print(cnt)

cnt = 0
for y in range(R):
    for x in range(C):
        if graph[y][x] == '#':
            dfs(x, y)
            cnt += 1
# print(graph)
print(cnt)