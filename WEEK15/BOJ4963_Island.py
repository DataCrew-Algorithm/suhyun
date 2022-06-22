import sys
sys.setrecursionlimit(100)
def dfs(x, y):

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < w) and (0 <= ny < h):
            if graph[ny][nx] == 1:
                graph[ny][nx] = -1
                dfs(nx, ny)

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 & h ==0:
        break
    else:
        graph =[]
        for _ in range(h):
            tmp = list(map(int, sys.stdin.readline().split()))
            graph.append(tmp)

        cnt = 0

        for y in range(h):
            for x in range(w):
                if graph[y][x] == 1:
                    dfs(x, y)
                    cnt += 1
        # print(graph)

        print(cnt)


