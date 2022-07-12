
# key error
import sys

T = int(sys.stdin.readline())

def dfs(v):
    global cnt, N
    cnt += 1

    if (graph[v] != N) & (cnt < N+1): # 타겟인 N이 아닐땐 dfs로 계속 돈다. 단, 한바퀴돌기전이어야 함
        dfs(graph[v])



for _ in range(T):
    cnt = 1
    N = int(sys.stdin.readline())
    graph = {} # 딕셔너리로 그래프 그리기
    tmp = []
    for _ in range(N):
        tmp.append(int(sys.stdin.readline()))

    for j in range(len(tmp)-1):
        graph[tmp[j]] = tmp[j+1]

    if len(tmp) ==1: #  1 1 1 해서 key가 없는 경우 해결
        cnt = 2
    else:
        dfs(tmp[0])

    # print(graph)
    if cnt == N+1:
        print(0)
    else: print(cnt)


