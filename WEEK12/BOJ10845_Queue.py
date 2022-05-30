# ver1 이중리스트 아닌풀이
from collections import deque
import sys
N = int(sys.stdin.readline())
queue = deque()

for _ in range(N):
    command = sys.stdin.readline().split()

    if len(command) == 2:
        queue.append(int(command[1]))

    else:
        command = command[0]
        if command == 'pop':
            if queue:
                print(queue.popleft())
            else:
                print(-1)

        elif command == 'size':
            print(len(queue))

        elif command == 'empty':
            if queue:
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