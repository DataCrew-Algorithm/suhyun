A, B = map(int, input().split())

num_list = []               # 1000번째 숫자까지 채워둠

# n이 n개씩 있으므로 1000번째 수는 45(1035번째 까지 45로 채워줌)
for i in range(1, 46):      # 1 ~ 45까지 반복
    for _ in range(i):      # n이 n개씩 있으므로
        num_list.append(i)
        
print(sum(num_list[A-1:B])) # 인덱스가 0부터 시작되므로 -1해줌