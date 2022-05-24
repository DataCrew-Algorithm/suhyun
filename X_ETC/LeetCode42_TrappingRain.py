class Solution:
    def trap(self, height):

        counter = 0
        # 최대층 부터
        max_num = max(height)
        max_count = height.count(max_num)

        for num in range(max_num, 0, -1): # 높은 층부터 
            left = 0
            right = len(height) - 1
            if max_count < 2:           # 최대 층의 값이 2개가 아니면 
                max_count += height.count(num)
            
            else:                           # 한개인 최대층을 제외한 각 최대층의 너비를 구함
                while left < right:
                    if height[left] < num:  # 작으면 왼쪽 포인터를 오른쪽으로 움직임
                        left += 1
                    else:
                        break
                    
                    if height[right] < num: # 오른쪽 포인터가 작으면 
                        right -= 1
                    else:
                        break


                print(left, right)
                
                for i in range(left+1, right): # 
                    if height[i] < num:
                        counter += 1
                        # print(counter)

        return counter

# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# # height = [4,2,0,3,2,5]
# sol = Solution()
# print(sol.trap(height))


                

height = [4,2,0,3,2,5]
sol = Solution()
print(sol.trap(height))



        





# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
#          [0, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 0]
# height = [4, 2, 0, 3, 2, 5]
#          [1+1+2+4]         