# import sys
# # sys.setrecursionlimit(10000)


# N = int(sys.stdin.readline())
# graph = []
# for _ in range(N):
#     graph.append(list(map(int, sys.stdin.readline().split())))




# def dfs(graph):
#     global row, col
#     jump = graph[row][col]
#     while (row + jump <= (N-1)) & (col + jump <= (N-1)):
#         row = row + jump
#         col = col + jump

# row = 0
# col = 0

# dfs(graph)
# print(row, col)
# print(graph[row][col])


# 그래프 변경
import sys

N = int(sys.stdin.readline())
map_ = []
for _ in range(N):
    map_.append(list(map(int, sys.stdin.readline().split())))   # 게임판의 구역 입력


graph = []
for n in range(N**2):       # graph 만들기 위한 dict 정의
    graph.append([])


num = -1
for i in range(N):                   # 
    for j in range(N):               # 
        if (i == N-1) & (j == N-1):  # 정사각형 밖으로 벗어나 버리면 break
            break
        else:
            num += 1
            if (j + map_[i][j]) <= (N-1):   # 원래있던 열값에서 써져있는 숫자를 더했을 때, 정사각형 밖으로 벗어나지 않으면
                col = j + map_[i][j]        # 그 숫자를 더해준 열을 반영하여
                graph[num].append((i, col)) # 그 순서쌍을 저장

            if (i + map_[i][j]) <= (N-1):   # 행도 똑같음
                row = i + map_[i][j]
                graph[num].append((row, j))
print(graph)

indices = []            # [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 번호표를 만드는 코드
num = 0
for x in range(N):
    tmp = []
    for y in range(N):
        num += 1
        tmp.append(num)
    indices.append(tmp)
print(indices)

graph_new = [[] for _ in range(N**2)]           # graph를 새로 만드는 코드
for i in range(len(graph)):                     # [[2, 4], [3, 5], [], [5, 7], [], [9], [9], [], []]
    for j in range(len(graph[i])):
        a, b = graph[i][j]
        graph_new[i].append(indices[a][b])

print(graph_new)

visited = [0] * (N **2 + 1)
def dfs(graph, start):      # dfs로 탐색
    visited[start] = 1
    for i in graph[start-1]:    # 그래프에서 0번 인덱스 자리에 1에 대한 값이 들어갔으므로 -1 해줌
        if visited[i] == 0:
            dfs(graph, i)

dfs(graph_new, 1)
print(visited)

if visited[N**2] == 1:      # 가장 마지막인 9번(2*2일때는 4번)이 1일때 승리하는 것임
    print('HaruHaru')
else:
    print('Hing')

