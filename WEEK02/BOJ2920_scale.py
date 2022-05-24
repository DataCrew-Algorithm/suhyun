
# dict_scale = {'1': 'c', '2': 'd', '3' : 'e', '4' : 'f', \
#     '5': 'g', '6': 'a', '7':'b', '8' : 'C'}

# reverse함수를 쓰려다가 헤맴. reverse함수는 그 리스트자체를 뒤집어주는 것임
# a = list_scale.reverse() 다른 변수에 저장해도 원래 리스트가 바뀌는것에 불과. 즉, a = None

# 입력받은 리스트와 만든리스트가 같은지 판별하는 방식

list_scale = [i for i in range(1,9)] # 1~8 리스트 생성

list_input = list(map(int, input().split())) 


if list_input == list_scale:
    print('ascending')

elif list_input == list_scale[::-1]:
    print('descending')

else:
    print('mixed')


