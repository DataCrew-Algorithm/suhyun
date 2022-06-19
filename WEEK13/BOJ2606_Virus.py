# DFS

from sys import stdin
read = stdin.readline
# 그래프를 만드는 과정
dic={}
comp = int(read())
for i in range(comp):
    dic[i+1] = set()
for j in range(int(read())):
    a, b = map(int,read().split())
    dic[a].add(b)
    dic[b].add(a) 

print(dic)

# # dfs를 구현하는 함수
# def dfs(start, dic):
#     for i in dic[start]:
#         if i not in visited:
#             visited.append(i)
#             dfs(i, dic)

# visited = []
# dfs(1, dic)
# print(len(visited)-1) #자기 자신인 1 제외

cnt = 0
def Dfs(v, dict, visited):
    global cnt
    visited[v] = 1
    for i in dict[v]:
        if not visited[i]:
            visited[i] = 1
            cnt += 1
            Dfs(i, dict, visited)
    return cnt

visited =[0] * (comp + 1)
print(Dfs(1, dic, visited))


