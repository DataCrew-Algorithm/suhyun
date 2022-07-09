import sys
sys.setrecursionlimit(100000000)
N = int(sys.stdin.readline())

graph = {}  # {0: [3], 1: [6], 2: [], 3: [4, 5], 4: [0], 5: [6], 6: [2]}
for i in range(N):
    tmp = []
    line = list(map(int, sys.stdin.readline().split()))
    for idx in range(len(line)):
        if line[idx] == 1:
            tmp.append(idx)
    graph[i] = tmp

print(graph)


def dfs(start, target):
    # start에서 부터 dfs로 돌아서 target으로 돌아오면 그자리에 1을 더하는 코드 작성
    # 딕셔너리 value 값을 하나씩 뽑으면서 도는 for문 작성해야
    if not graph[start]:
        for i in graph[start]:
            # print(i, target)
            if i == target: # target이랑 같으면 종료 1
                return 1
            
            # elif i == None:
            #     return 0

            else:
                return dfs(i, target) # visited 같은 담아주는 것이 없을 때에는 return 으로 담아줘야함
            # if i == start: # 처음으로 돌아오면 종료 0
            #     return 0
            # else:
            #     dfs(i, target)

# print(dfs(6,6))

result = [[0] * N for _ in range(N)]
print(result)

for y in range(N):
    for x in range(N):
        result[y][x] = dfs(x, y)
    # print(*result[y])
print(result)
# for i in range(N):
#     print(*result[i])

#

import sys


# dfs 탐색
def dfs(v):
    # 한줄씩 비교
    for i in range(n):
        if check[i] == 0 and graph[v][i] == 1:
            check[i] = 1
            dfs(i)


n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for x in range(n):
    # 체크 리스트를 초기화하여 수행
    check = [0 for _ in range(n)]
    dfs(x)
    print(*check) # 리스트의 경우에는 *기호를 넣어서 각각의 값을 출력할 수 있다.
