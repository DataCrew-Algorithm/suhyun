# 문자열을 뒤에서 부터 읽는 함수를 정의
def reverse_read(x):
    x = str(x)          # 함수의 인자를 int로 받아서 str으로 바꿔준 것임.
    x_r = int(x[::-1])       # 슬라이싱을 쓰기 위해서, 그리고 비교를 위해 숫자로 바꿈
    
    return x_r

num_1, num_2 = map(int, input().split()) # map을 빼도 스트링을 따로 저장하고 스트링도 크기비교가능
renum_1 = reverse_read(num_1)
renum_2 = reverse_read(num_2)

print(max(renum_1, renum_2))




# 풀이 2 합까지 같이 구하는 함수 만들기
def max_reverse_read(x, y):
    x = str(x)
    x_r = int(x[::-1])
   
    y = str(y)
    y_r = int(y[::-1])
    

    if x_r >= y_r:
        return x_r

    else:
        return y_r

num_1, num_2 = map(int, input().split())
print(max_reverse_read(num_1, num_2))





# num_list = list(input().split())


# for idx in range(len[num_list]):
#     for i in num_list[idx][::-1]:


# print(first_num)


