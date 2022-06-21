import sys
n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
m = int(sys.stdin.readline())
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())

    graph[x].append(y)
    graph[y].append(x)

print(graph)


# 처음에 했던 잘못된 풀이
def dfs(start, cnt):
    ans = -1
    visited[start] = 1          # 출발점에 visited를 바꿔줌. 여기서는 visited의 7번을 1로 바꿔줌

    if start == b:              # 이렇게 같아지는 순간에 cnt를 출력하고 싶은데 
        ans = cnt              # 재귀함수에서 원하는 순간에 탈출 불가능(끝까지 탐색해야함) -> 그 과정에서 ans가 바뀜
        # print(ans)

    for i in graph[start]:
        if visited[i] == 0:
            cnt += 1
            dfs(i, cnt)    
    return ans 

# 잘못된 답안

visited = [0] * (n+1)
answer = dfs(a, 0)

print(answer)



# ans = []

# def dfs(start, cnt):
#     cnt += 1                    # 재귀함수를 실행할 때마다 1씩 더해주는 코드를 작성
#     visited[start] = 1          # 출발점에 visited를 바꿔줌. 여기서는 visited의 7번을 1로 바꿔줌

#     if start == b:              # 리스트로 받아준 다음에 0번 인덱스를 찍어주는 방식
#         ans.append(cnt)         
#         # print(ans)

#     for i in graph[start]:
#         if visited[i] == 0:
#             dfs(i, cnt)             
#     return ans

# visited = [0] * (n+1)
# answer = dfs(a, 0)

# if answer:
#     # print(answer-1)
#     print(answer[0]-1)

# else:
#     print(-1)

# print(visited)





