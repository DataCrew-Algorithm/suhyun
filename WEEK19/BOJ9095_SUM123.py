import sys
# from itertools import combinations
read = sys.stdin.readline

T = int(read())

def fac(n):         # factorial 구현
    if n > 1:
        return n * fac(n-1)
    else:
        return 1

# 1 * a + 2 * b + 3 * c
# a,b,c를 구하는 것은 1,2,3이 몇개씩 있는지를 구하는 것
# 조합을 먼저 구한다음에, 그에 대한 '같은 것을 포함한 순열'을 구하는 방식

def sums(target):
    num_comb = []
    for c in range(int(round(target/3))+1): # a = 0, b = 0, c의 최댓값
        for b in range(int(round(target/2))+1):
            for a in range(target+1):
                if  (a + 2 * b + 3 * c) == target:
                    num_comb.append([a, b, c])
    return num_comb



for _ in range(T):
    perms = 0
    target = int(read())
    combs = sums(target)
    # print(combs)
    for comb in combs: # 각 조합마다 '같은것을 포함한 순열'의 갯수 구해서 누적 합하기
        tmp = fac(sum(comb)) / (fac(comb[0]) * fac(comb[1]) * fac(comb[2]))
        perms += int(tmp)
    print(perms)

    