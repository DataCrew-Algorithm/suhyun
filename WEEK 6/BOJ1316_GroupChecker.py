N = int(input())

def checker(str):
    counter = 0
    alpha_list = [str[0]]
    
    for a in range(1, len(str)):
        if str[a] != str[a-1]:
            if str[a] in alpha_list:
                counter -= 1
                break
            else: 
                alpha_list.append(str[a])

    return counter
            

ans = 0
for _ in range(N):
    ans += checker(input())

print(ans+N)
