N = input()

count = 1
N = N.zfill(2)
new_N = N
while True:
    tmp1 = str(int(new_N[0]) + int(new_N[1]))
    tmp1 = tmp1.zfill(2)
    # print(tmp1)
    tmp2 = new_N[-1] + tmp1[-1]
    print(tmp2)
    if tmp2 == N:
        break
    else:
        new_N = tmp2.zfill(2)
        count += 1

print(count)





