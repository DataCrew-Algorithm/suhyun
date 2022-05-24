# 알파벳 리스트를 만들고
# find 메서드를 써서, 찾으면 거기에 인덱스 넘버를, 없으면 -1이 나오게함
# find 함수가 그 문자열에서 나오는 첫번째 인덱스를 반환하므로 충분.

ans = [0] * 26
list_alpha = list('abcdefghijklmnopqrstuvwxyz')

word = input()

for i in range(0, 26):
    ans[i] = word.find(list_alpha[i])
    
# list에도 join 메서드를 쓸수 있음. 다만 리스트안에 값들이 str이어야 함.
str_ans = list(map(str, ans)) # join 메서드를 쓰기 위해서 리스트의 각 값을 문자열로 변경

print(' '.join(str_ans)) # 리스트를 대괄호 없이 출력하기 위해서 join 함수 씀 



# for i, alpha in enumerate(list_alpha): # 인덱스와 값을 순차적으로 반환
#     ans[i] = word.find(alpha)











ss = map(str, ans) # map은 iterator - list,tuple 등으로 만들기 전 단계
print(ss.__next__())
print(ss.__next__())




# list_ans = list(map(str, ans)) # list에도 join 메서드를 쓸수 있음. 다만 리스트안에 값들이 str이어야 함.
# print(' '.join(list_ans))


# for i, alpha in enumerate(list_alpha): # 인덱스와 값을 순차적으로 반환
#     ans[i] = word.find(alpha)