# 풀이 1 (sort 사용)

N = input()                 # 숫자를 입력받음

str_list = list(N)          # 한 글자씩 분리해서 리스트에 넣음

str_list.sort(reverse=True) # 내림차순으로 정렬

print(''.join(str_list))    # 다시 합쳐줌




# 풀이 2 (퀵정렬을 이용한 풀이)

N = list(input())

# N = [6,1,4,2,3]
# [lesser list ]         ||       [eqaul_list ]             || [greater_list]
# pivot = 4 (len(N)을 2로 나눈 몫은 2, N[2]=4) 
# 4보다 작으면 lesser_list, 4보다 크면 greater_list, 같으면 equal_list에 각각 포함
# lesser_list와 greater_list 각각에 대해서도 퀵정렬 반복한다.


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    lesser_list, greater_list, equal_list = [], [], []
    for num in arr:
        if num < pivot:
            lesser_list.append(num)
        elif num > pivot:
            greater_list.append(num)

        else:
            equal_list.append(num)

    return quick_sort(lesser_list) + equal_list + quick_sort(greater_list)

answer = quick_sort(N)[::-1]
print(''.join(answer))