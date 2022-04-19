def classy(num1, num2):

    if num2 % num1 == 0:
        print('factor')
    elif num1 % num2 == 0:
        print('multiple')
    else:
        print('neither')


while True:
    num1, num2 = map(int, input().split())
    if num1 == 0 & num2 == 0:
        break
    else: classy(num1, num2)
    

