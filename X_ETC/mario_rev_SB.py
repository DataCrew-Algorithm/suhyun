mushroom = [int(input()) for _ in range(10)]

sum1 = mushroom[0]      
sum2 = sum1 + mushroom[1]            
sum3 = sum2 + mushroom[2]       
sum4 = sum3 + mushroom[3]           
sum5 = sum4 + mushroom[4]          
sum6 = sum5 + mushroom[5]           
sum7 = sum6 + mushroom[6]          
sum8 = sum7 + mushroom[7]          
sum9 = sum8 + mushroom[8]
sum10 = sum9 + mushroom[9]           
# sum이 한개가 부족해서 만들었어요. 이 경우에는 sum0부터 sum9까지 하는게 보기 편하실 것 같아요.
# for문 써서 i += 더할값 -> 해서 누적합 만드는게 제일 베스트 이긴 합니다.

sum_all = [sum1, sum2, sum3, sum4, sum5, sum6, sum7, sum8, sum9, sum10]

rest = []            
for i in range(10): # sum10까지 총 10개라서 10으로 바꿨어요.
    rest.append(abs(sum_all[i] - 100))

rest = rest[::-1] # 뒤집어서 인덱스 찾았으니

result = rest.index(min(rest))
sum_all = sum_all[::-1] # 이것도 뒤집어서 찾아야 합니다.

result = sum_all[result]    
# result라는게 48줄에서는 index였다가 리스트의 인덱싱 값으로 바뀌어서 헷갈릴 소지가 있어, 다른 변수로 지정하는게 좋아보여요.
print(result)