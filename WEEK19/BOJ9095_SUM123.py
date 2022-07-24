import sys
# from itertools import combinations
read = sys.stdin.readline

T = int(read())

def fac(n):
    if n > 1:
        return n * fac(n-1)
    else:
        return 1

# 1 * a + 2 * b + 3 * c
def sums(target):
    num_comb = []
    for c in range(int(round(target/3))+1):
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
    for comb in combs:
        tmp = fac(sum(comb)) / (fac(comb[0]) * fac(comb[1]) * fac(comb[2]))
        perms += int(tmp)
    print(perms)

    