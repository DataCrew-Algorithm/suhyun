sentence = list(input())
# print(sentence)

left = 0
right = 0
while left < len(sentence):
    if sentence[left] == '<':               # < 를 만났을 때,
        while sentence[left] != '>':        # > 를 만날 때까지 왼쪽포인터 +1
            left += 1
        left += 1


    elif sentence[left].isalnum():          # 문자, 숫자를 만났을 때, 이 때만 뒤집음
        # print(f'left:{left}')
        right = left
        while True:
            try:
                if sentence[right].isalnum():
                    right += 1
                    # print(right)
                else: break
            except: break

        tmp = sentence[left:right]
        tmp.reverse()
        sentence[left:right] = tmp

        # print(sentence)
        left = right + 1 

    elif sentence[left] == ' ':              # 띄어쓰기를 만났을 때, 왼쪽포인터만 +1
        left += 1

ans = ''.join(sentence)
print(ans)