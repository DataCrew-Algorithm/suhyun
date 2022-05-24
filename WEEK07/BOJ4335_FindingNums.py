

def judging(nums, mentions):
    possible = [1,2,3,4,5,6,7,8,9,10]
    ans = possible

    for i in range(len(nums)):
        # if not ans:
        #     break
        
        if mentions[i] == 'too high':
            ans = set(ans) & set(possible[:nums[i]-1])

        elif mentions[i] == 'too low':
            ans = set(ans) & set(possible[nums[i]:])

        elif mentions[i] == 'right on':
            tmp = possible[nums[i]-1]
        
    # print(ans)
    # print(tmp)
    
    if tmp in ans:
        return print('Stan may be honest')
    else:
        return print('Stan is dishonest')




nums = []

while True:
    nums = []
    mentions = []
    while True:
        num = int(input())
        if num == 0:
            break
        mention = input()
        

        nums.append(num)
        mentions.append(mention)
        if mention == 'right on':
            break
    # print(nums)
    # print(mentions)
    if num == 0:
        break
    judging(nums, mentions)

    
    




# for _ in range(mentions.count('right on')):


#     judging(nums, mentions)
    


    # if mentions[-1] == 'right on':
    #     break



             



