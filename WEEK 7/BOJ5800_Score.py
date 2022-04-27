K = int(input())

def gap(l):
    p1 = 0
    p2 = 1
    max_gap = abs(l[p1]-l[p2])
    
    while p2 < len(l)-1:
        tmp = max_gap
        p1 += 1
        p2 += 1
        new = abs(l[p1]-l[p2])
        if tmp < new:
            max_gap = new
    return max_gap
        



def stats(l, i):
    la_gap = gap(l)
    return print(f'Class {i+1}'), print(f'Max {max(l)}, Min {min(l)}, Largest gap {la_gap}')

for i in range(K):
    class_list = list(map(int, input().split()))
    num = class_list[0]
    class_list = class_list[1:]
    class_list.sort(reverse = True)
    

    stats(class_list, i)
    


