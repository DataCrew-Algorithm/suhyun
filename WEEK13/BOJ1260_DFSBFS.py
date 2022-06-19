# # 실패..
# from sys import stdin
# from collections import deque

# N, M, V = map(int, stdin.readline().split())
# dict = {}
# for i in range(N):
#     dict[i+1] = set()

# for _ in range(M):
#     a, b = map(int, stdin.readline().split())
#     dict[a].add(b)
#     dict[b].add(a)
#     dict[a] = set(sorted(dict[a]))
#     dict[b] = set(sorted(dict[b]))
# print(dict)

# def dfs(V, dict):
#     for j in dict[V]:
#         if j not in visited1:
#           visited1.append(j)
#           dfs(j, dict)
#     return visited1



# def bfs(V, dict):
#     queue = [V]
#     while queue:
#         for k in dict[queue.pop()]:
#             if k not in visited2:
#                 visited2.append(k)
#                 queue.append(k)
                
#     return visited2

# visited1 = [V]
# print(*dfs(V, dict), end = " ")
# print()
# visited2 = [V]
# print(*bfs(V, dict), end = " ")




# from sys import stdin
# from collections import deque
# import sys
# sys.setrecursionlimit(10**7)

# N, M, V = map(int, stdin.readline().split())
# dict = {}
# for i in range(N):
#     dict[i+1] = set()

# for _ in range(M):
#     a, b = map(int, stdin.readline().split())
#     dict[a].add(b)
#     dict[b].add(a)
#     dict[a] = set(sorted(dict[a]))
#     dict[b] = set(sorted(dict[b]))
# print(dict)

# def dfs(V, dict):
#     visited1 = [V]

#     for j in dict[V]:
#         if j not in visited1:
#           visited1.append(j)
#           dfs(j, dict)

# def bfs(V, dict):
#     visited2 = [V]
#     queue = [V]
#     while queue:
#         for k in dict[queue.pop()]:
#             if k not in visited2:
#                 visited2.append(k)
#                 queue.append(k)
                
# print(dfs(V, dict))
# print()
# print(bfs(V, dict))
# # print(*dfs(V, dict, visited), end = " ")
# # print()
# # print(*bfs(V, dict, visited), end = " ")


# 블로그 풀이
from collections import  deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

print(graph)
visited = [False] * (n + 1)

def Dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            Dfs(graph, i, visited)

def Bfs(graph, v, visited):
    visited = [False] * (n + 1)
    queue = deque([v])
    visited[v] = True
    while queue:
        pop = queue.popleft()
        print(pop, end=' ')
        for i in graph[pop]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

Dfs(graph, v, visited)
print()
Bfs(graph, v, visited)