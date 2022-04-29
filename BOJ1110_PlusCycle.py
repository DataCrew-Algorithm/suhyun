N = input()

count = 1
N = N.zfill(2)    # 한자리수가 들어오면 앞을 0으로 채움
new_N = N
while True:
    tmp1 = str(int(new_N[0]) + int(new_N[1]))
    tmp1 = tmp1.zfill(2)                        # 각 자리수의 합이 한자리수 이면 앞을 0으로 채움
    # print(tmp1)
    tmp2 = new_N[-1] + tmp1[-1]
    # print(tmp2)
    if tmp2 == N:                               # 최초에 받았던 값과 같으면 종료
        break
    else:
        new_N = tmp2.zfill(2)
        count += 1

print(count)





