# 5x+3y= N
# x + y개수의 최소화
# x, y 만족하는 정수 없으면 -1 출력

# 1st 5의 개수 최대화 하고 3의 개수 해서 가능한지 찾는다
# 2nd 3의개수 적절히 조정해서 가능한지 찾는다
# 3rd 아예 불가능인지 찾는다.




# 5x + 3y = N
# x + y의 최소화

# trial & error 방법 N // 5 -> x의 최대값, N// 3 -> y의 최대값
ans_list = []
N = int(input())



for num_5 in range((N // 5)+1):         # num_5 최댓값은 5로 나눈 몫임
    for num_3 in range((N // 3)+1):       # num_3 최댓값은 3으로 나눈 몫임
        if num_5 * 5 + num_3 * 3 == N:      # 5, 3에 번갈아 넣으면서 N과 일치하면
            ans_list.append(num_5+num_3)    # 더한 값을 정답에 넣음

try:
    print(min(ans_list)) # 리스트가 비어있지 않아서 실행이 되면,
except:                  # 리스트가 비어서 min 못한다고 나오면,
    print(-1)



  
# if ans_list == None:
#     print(-1)
# else:

    
# 풀이2: 5만 역으로 돌려서 맞으면 break
# 5의 개수를 최댓값부터 돌리고, 3의개수는 작은수부터 돌리면, 일치하는 순간이 곧 두개의 개수가 
# 최소가 되는 순간임
N = int(input())
ans = 0

for num_5 in range((N // 5), -1, -1):       # num_5 가능한 최댓값은 5로 나눈 몫임
    for num_3 in range((N // 3)+1):         # num_3 가능한 최댓값은 3으로 나눈 몫임
    
    
        if num_5 * 5 + num_3 * 3 == N:      # 5, 3에 번갈아 넣으면서 N과 일치하면
            ans = num_5 + num_3             # 더한 값을 정답에 넣음
            break                           # 가까운 for문인 num_3에 대한 것 탈출
    if ans:             # ans에 0이 아닌 값이 있으면, 첫번째 for문 탈출
        break

if ans == 0:
    print(-1)
else:
    print(ans)
