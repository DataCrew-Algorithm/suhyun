# import sys

# T = int(sys.stdin.readline())
# # for 문으로 마지막에 T번 반복하는 코드 작성해야함

# M, N, K = map(int, sys.stdin.readline().split())
# graph =[]

# for _ in range(N):  # 0으로 가득찬 이중 리스트 만들기
#     row = [0]*M
#     graph.append(row)

# for _ in range(K):  # 
#     a, b = map(int, sys.stdin.readline().split())
#     graph[b][a] = 1
# print(graph)
# visited = []
# def dfs(graph, i, j):
    
#     while (i <= N-1) & (j <= M-1):
#         if (graph[i][j] == 1) & ([i,j] not in visited):
#             visited.append([i,j])
#             print(visited)
#             dfs(visited, i+1, j)    # 오른쪽 +1
#             dfs(visited, i, j+1)    # 아래쪽 +1

#     return visited



# cnt = 0

# for i in range(N):
#     for j in range(M):
#         tmp = dfs(graph, i, j)
#         print(tmp)
#         if len(tmp) >= 1:
#             cnt += 1


# 티스토리 풀이

# 재귀 limit 설정
import sys
sys.setrecursionlimit(10000)

### 2
# dfs 정의
def dfs(x, y):
    # 상하좌우 확인을 위해 dx, dy 생성
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    

    # 네 방향 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < M) and (0 <= ny < N):  # nx:ny ↔ M:N 범위 참고
            if graph[ny][nx] == 1:
                graph[ny][nx] = -1  # 배추가 인접할 때 체커
                print(graph)
                dfs(nx, ny)
                

### 1                    
T = int(input())
# T = int(sys.stdin.readline())
for i in range(T):
    M, N, K = map(int, input().split())  # M:가로, N:세로, K:개수
    # M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0]*M for i in range(N)]
    cnt = 0

    # 배추 위치에 1 표시 (그래프 만들기)
    for j in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1
    # print(graph)

### 3        
    # dfs 활용해서 배추 그룹 수 세기
    for x in range(M):
        for y in range(N):
            if graph[y][x] == 1:
                dfs(x, y)
                cnt += 1

    # print(graph)
    # 정답을 위한 출력
    print(cnt)









