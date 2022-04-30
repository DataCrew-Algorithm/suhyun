# # 알파벳 리스트를 만들고
# # find 메서드를 써서, 찾으면 거기에 인덱스 넘버를, 없으면 -1이 나오게함
# # find 함수가 그 문자열에 첫번째 값을 찾으므로 충분.

# ans = [0] * 26
# list_alpha = list('abcdefghijklmnopqrstuvwxyz')

# word = input()

# for i, alpha in enumerate(list_alpha):
#     ans[i] = word.find(alpha)
    
# str_ans = map(str, ans) # join 메서드를 쓰기 위해서 리스트를 문자열로 변경

# print(' '.join(str_ans)) # 리스트를 대괄호 없이 출력하기 위해서 문자열의 join 함수 씀

# a =15
# print(a // 3)

# print(4//5)

# a  = [7,4,3,5,1,8]

# a.sort()
# print(a)
# b = set(a)
# print(b)
# c = list(b)
# print(c)
# c.sort()


# Ver.1 (108ms)

# num = int(input())
# arr = [int(input()) for _ in range(num)]
# arr = sorted(arr) # sort(arr) 도 가능: 이 경우 객체 재지정 필요 없음
# print(type(*arr))

# a = [1,2,3,4]
# print(a[-2:])

# for i in range(5, 0, -1):
#     print(i)

# l = ['1','2','3','4']
# print(max(l))
# l[2] =7
# print(l)


# text = '0'
# a = text.zfill(2)
# print(a), print(a)
# print(type(a))

# n = '26'
# b = '26'
# print(n == b)


# a = [1,2,3,4,5,'a', 'a', 'a']
# print(a.count('a'))

# nums = []
# print(nums[-1])

nums = [1,2,3,4]
a = nums
print(a)
a.append(5)
print(nums)