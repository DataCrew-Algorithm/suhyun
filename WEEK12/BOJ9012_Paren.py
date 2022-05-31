import sys
T = int(sys.stdin.readline())

for _ in range(T):
    PS = sys.stdin.readline().rstrip()
    stack = []
    for i in range(len(PS)):
        if stack:
            if (PS[i] != stack[-1]) and (stack[0] != ')'):
                stack.pop()
                # print(f'pop:{stack}')

            else:
                stack.append(PS[i])
                # print(f'app o: {stack}')

        else:
            stack.append(PS[i])
            # print(f'app em:{stack}')
    if not stack:
        
        print('YES')
    else:
        print('NO')
