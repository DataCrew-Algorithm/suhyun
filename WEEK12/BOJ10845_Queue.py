# ver1 이중리스트 아닌풀이
from collections import deque
import sys
N = int(sys.stdin.readline())
queue = deque()

for _ in range(N):
    command = sys.stdin.readline().split() # ['pop']

    if len(command) == 2:               # push 1 일때만 리스트의 길이가 2임
        queue.append(int(command[1]))

    else:
        command = command[0]            # 길이가 1일때는 str으로 바꿔서 넣음
        if command == 'pop':            
            if queue:
                print(queue.popleft())
            else:
                print(-1)

        elif command == 'size':
            print(len(queue))

        elif command == 'empty':
            if queue:                   # 빈리스트 이면 0
                print(0)
            else:
                print(1)

        elif command == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)

        elif command == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)


# ver2 이중리스트

# from collections import deque
# import sys
# N = int(sys.stdin.readline())
# queue = deque()
# commands = [sys.stdin.readline().split() for _ in range(N)]
# for command in commands:
#     if len(command) == 2:
#         queue.append(int(command[1]))

#     else:
#         command = command[0]
#         if command == 'pop':
#             if queue:
#                 print(queue.popleft())
#             else:
#                 print(-1)

#         elif command == 'size':
#             print(len(queue))

#         elif command == 'empty':
#             if queue:
#                 print(0)
#             else:
#                 print(1)

#         elif command == 'front':
#             if queue:
#                 print(queue[0])
#             else:
#                 print(-1)

#         elif command == 'back':
#             if queue:
#                 print(queue[-1])
#             else:
#                 print(-1)