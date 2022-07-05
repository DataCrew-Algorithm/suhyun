# 80ms
import sys

sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())

graph = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
# print(graph)

def dfs(x, y):
    global cnt      # 재귀함수를 써야하기때문에 계속 재정의 되면 안되므로 cnt를 밖으로 빼고 global해줌
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for n in range(4):    
        nx = x + dx[n]
        ny = y + dy[n]
        if (0 <= nx< N) & (0 <= ny < N):
            # print(nx, ny)
            if graph[ny][nx] == '1':
                graph[ny][nx] = '2'
                dfs(nx,ny)
                cnt += 1            # 해당 값이 1이어서 dfs로 움직일때 마다 1을 더해줌


result = []
for j in range(N):
    for i in range(N):
        if graph[j][i] == '1': # 정사각형을 돌면서 1일때만 탐색
            graph[j][i] = '2'   # 2로 바꿔주고
            cnt = 1             # 단지 하나를 발견했으니 1로 시작
            dfs(i, j)
            result.append(cnt)

print(graph)
result.sort()           # 오름차순으로 정리
print(len(result))      
for i in range(len(result)):
    print(result[i])

# print(*result, sep = '\n')
