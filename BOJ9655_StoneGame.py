# 3개 돌은 1개 돌로 치환할 수 있음.
# 3개 하나씩 짝지으면, 홀/짝에 따라서 먼저한 사람이 이길지 질지가 정해짐

# 마지막에 누가 했는지를 고르는게 중요(두 사람 A, B)
# O O O -> A, B, A  결국 먼저 한 사람이 마지막에 한것
# O -> A 먼저한 사람이 곧 마지막에 한 것
# 3개를 한개로 치환. 무한히 치환 가능. 결국, 돌이 1개일때, 2개일 때의 케이스만 알면된다.



N = int(input())

if N % 2 == 0:
    print('CY')

else:
    print('SK')