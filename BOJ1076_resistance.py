color_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
input_list = []
first_, second_, third_ = 0, 0, 0
for _ in range(3):
    input_list.append(input())

first_ = color_list.index(input_list[0])
second_ =color_list.index(input_list[1])
third_ = color_list.index(input_list[2])

ans = (first_*10 + second_)*10**third_
print(ans)

