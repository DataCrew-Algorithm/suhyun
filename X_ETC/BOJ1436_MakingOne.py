X = int(input())
count = 0
while X > 1:
    if X % 3 == 0:
        while X % 3 == 0:
            X = X / 3
            count += 1
        if X == 1: break

    elif X % 2 == 0:
        while X % 3 == 0:
            X = X / 2
            count += 1
        if X == 1: break

    else:
        while (X % 3 != 0) or (X % 2 != 0):
            X -= 1  
            count += 1
        if X == 1: break
print(count)