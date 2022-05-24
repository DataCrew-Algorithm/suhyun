K = int(input())
# 투포인터 처럼?
def gap(l):                     # 리스트를 받음  
    p1 = 0                      
    p2 = 1
    max_gap = abs(l[p1]-l[p2])
    
    while p2 < len(l)-1:            # 5 30 25 76 23 78
        tmp = max_gap           
        p1 += 1                     # 인접한 합을 연속적으로 구하므로 p1, p2 같이 증가해야함
        p2 += 1         
        new = abs(l[p1]-l[p2])      
        if tmp < new:               # 원래 있던 max_gap보다 커질때 
            max_gap = new           # max_gap을 새로운 값으로 갱신
    return max_gap
        

# Class 1
# Max 78, Min 23, Largest gap 46

def stats(l, i): # 리스트와 몇번째 Class인지를 받음
    la_gap = gap(l)
    return print(f'Class {i+1}'), print(f'Max {max(l)}, Min {min(l)}, Largest gap {la_gap}')



for i in range(K):
    class_list = list(map(int, input().split()))
    num = class_list[0]                 # 의미없음
    class_list = class_list[1:]         
    class_list.sort(reverse = True)     # 내림차순으로 정렬
    
    stats(class_list, i)
    


