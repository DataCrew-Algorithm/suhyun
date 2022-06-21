# 그냥 풀이
# import sys
# T = int(sys.stdin.readline())

# for _ in range(T):
#     N, M = map(int, sys.stdin.readline().split())
#     graph = [[0] * (N+1) for _ in range(N)]
    
#     for __ in range(M):
#         a, b = map(int, sys.stdin.readline().split())
#         a = graph.append(b)
#         b = graph.append(a)

#     print(N-1)

# dfs를 이용한 풀이
import sys
# sys.setrecursionlimit(10000)

def dfs(idx, cnt):
    visited[idx] = 1 # 출발점의 visited 값을 1으로 바꿔줌 visited = [0,1,0,0]
    for i in graph[idx]:
        if visited[i] == 0: # 방문 했던 것이면 그냥 넘기고, 방문 안했던 국가면 깊이 탐색
            cnt = dfs(i, cnt+1)
    return cnt


T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)] # 방향성이 없으므로 행렬 표현이 아닌 방식, 노드가 1부터 시작하므로 N+1

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    print(graph)
    visited = [0] * (N+1) # visited = [0,1,0,0]

    ans = dfs(1, 0)
    print(ans)



        
 