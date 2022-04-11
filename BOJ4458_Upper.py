
str_list = []       # 문장을 받아서
first_word = []     # 그 문장의 제일 첫단어를 한글자씩 리스트에 담고,
ans_list = []       

N = int(input()) # 개수를 입력 받음
for _ in range(N):                  # N번 동안 입력을 받고 다음을 반복
    str_list = input().split()      # 띄어쓰기를 기준으로 나눠서 리스트에 str으로 넣음
    first_word = list(str_list[0])  # 0번째 원소를 가져와서 한글자씩 쪼개어 리스트로 만듦
    first_word[0] = first_word[0].upper()   # 첫글자를 대문자로 바꿈

    str_list[0] = "".join(first_word)       # 한글자씩 쪼개진 리스트를 다시 합쳐서 원래 문장 리스트에 넣음
    ans_list.append(" ".join(str_list))     # 단어별로 쪼개진 리스트를 띄어쓰기를 넣어서 다시 하나의 문장으로 합침

for i in range(len(ans_list)):              # 정답 리스트의 길이만큼 돌면서
    print(ans_list[i])                      # 출력



