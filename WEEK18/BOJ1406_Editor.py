# ver1 시간초과
import sys
read = sys.stdin.readline

def editor(command):
    global p    # 커서가 몇번째에 있는지를 알려주는 변수

    if (command[0] == 'L') & (p != 0):  # 왼쪽 커서 이동은 -1. 단, 맨 왼쪽에 있지 않아야.
        p -= 1

    elif (command[0] == 'D') & (p != len(s)+1): # 왼쪽 커서 이동은 +1. 단, 맨 오른쪽에 있지 않아야.
        p += 1

    elif command[0] == 'P':
        s.insert(p, command[1]) # p자리에 넣음
        p += 1  # 그자리에 넣었으니 p는 한자리 오른쪽 이동해야함(왼쪽에 추가니까)
    
    elif (command[0] == 'B') & (p != 0):
        del s[p-1] # 왼쪽을 삭제해야해서 p-1
        p -= 1

s = list(read().rstrip())
N = int(read())
p = len(s)

# command = ['P', 'x']
# s.append(command[1])


for _ in range(N):
    command = list(read().rstrip().split()) # ['P', 'x']
    editor(command)
    # print(p)

print(''.join(s))

# ver.2 블로그풀이 참고 stack 두개를 이어서 푸는 풀이

import sys

st1 = list(sys.stdin.readline().rstrip())
st2 = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':   # 커서를 왼쪽으로 움직일때는 st1끝에서 빼서 st2끝에 넣음
        if st1:
            st2.append(st1.pop())
            
    elif command[0] == 'D':   # 커서를 오른쪽으로 움직일때는 st2끝에서 빼서 st1끝에 넣음
        if st2:
            st1.append(st2.pop())

    elif command[0] == 'B':  # 왼쪽 끝에 놈을 날린다
    	if st1:
            st1.pop()
            
    else:
    	st1.append(command[1]) # ['P', 'x'] <- x를 넣는다. 커서 왼쪽이므로 st1에
        
st1.extend(reversed(st2))
print(''.join(st1))

'''
abcd|
abcdx|
abcd | x
abcdy | x

abc|
ab | c
a | cb
|cba
x|cba
|cbax
x|cba
xy|cba
xyabc

'''