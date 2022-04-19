color_list = ['black', 'brown', 'red', 'orange', 'yellow', 
'green', 'blue', 'violet', 'grey', 'white']

input_list = []
first_, second_, third_ = 0, 0, 0   
# 값이 순서대로 인덱스라서 그 인덱스를 담을 변수 초기화

for _ in range(3):
    input_list.append(input())

first_ = color_list.index(input_list[0])
second_ = color_list.index(input_list[1])
third_ = color_list.index(input_list[2])

ans = (first_ * 10 + second_) * 10 ** third_ 
# 앞의 숫자는 이어서 적고, 뒤에 숫자는 10^(n)으로 구해져서 둘을 곱하면 답임
print(ans)

