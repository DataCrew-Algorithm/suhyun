def plus_stars(lst): # 이전 번(n-1)의 원소 앞 뒤에 '* ' ' *'를 추가하는 함수
    for j in range(len(lst)):
        lst[j] = '* '+ lst[j] + ' *' # 원래 리스트에 추가해서 담음
    return lst

def stars(n):
    if n == 1:
        return ['*']
    else:
        add1 = '*' * (4 *(n-1)+1)               # 위 아랫줄에 추가 4(n-1) + 1
        add2 = '*' + ' '*(4 * (n-1)-1) + '*'
        return [add1, add2] + plus_stars(stars(n-1)) + [add2, add1]

N = int(input())
print(*stars(N), sep = '\n')
    # add1 + '\n' + add2 + '\n'+ stars(n-1) + '\n' +add1 + '\n' + add2

# star_list = []
        # for i in range(4*(n-2)+1):
        #     stars(n-1)[i] = '* ' + stars(n-1)[i] + ' *'
        #     star_list.append('* ' + stars(n-1)[i] + ' *')
        # print(star_list)



# print('*****\n'
# '*   *')