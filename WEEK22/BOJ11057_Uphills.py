import sys
input = sys.stdin.readline

N = int(input())

hills = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1]*10]

def uphills(N):
    if N > 1:
        for i in range(2, N+1): # 2부터 N까지 만들기
            tmp = 0
            hills.append([])
            for j in range(10): # 10까지
                tmp += hills[i-1][j]
                hills[i].append(tmp)
    return sum(hills[N])

print(uphills(N)%10007)

'''
0: 0
1: 0, 1
2: 0, 1, 2

맨뒤가 해당 수 일때, 
  0 1 2 3 4 5 6 7 8 9   -> 맨 뒤에 오는 수
0 1 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1   -> #
2 1 2 3 4 5 6 7 8 9 10  -> #0 #1 ... #9
3 1
N

#0 1 
#1 1+1
#2 1+1+1

##0 1
##1 1+2
##2 1+2+3
##3 1+2+3+4

##9 1+2+3+..+10

####0 1
####1 

1 3 6 10 15 21 28 36 45 
9 16 21 24 25 24 21 16 9 


'''