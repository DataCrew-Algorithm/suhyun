# 빈병으로 반복해서 새 병으로 바꿀 수 있다는 점이 포인트
# 몫, 나머지 순서로 출력

# 3개를 1개로 바꿈
# 9 0 - 초기값      
# 3 0
# 1 0

# 2개를 1개로 바꿈
# 10 0 
# 5  0
# 2  1
# 1  1
# 1  0

# 몫이 1 보다 작아질 때 까지 반복해서 몫을 더해줌

empty_1, empty_2, div = map(int, input().split())

quo = empty_1 + empty_2
quo_sum = 0 
residual = 0

# 비교를 하는 등의 이유로 값을 담고 있을 필요가 없으면, 리스트에 안담아 줘도 된다.
while quo >= 1:
        
    quo, residual = divmod((quo + residual), div) # 몫, 나머지 동시 출력
    print(type(quo))
    quo_sum += quo # 초기값 제외 몫 다 더함

print(quo_sum)

