
# 투포인터를 이용한 풀이
class Solution:
    def twoSum(self, nums, target):
        left = 0
        right = len(nums)-1
        nums_s = sorted(nums)   # sort 해놓은 것을 새로 담음
        while left < right:

            if nums_s[left] + nums_s[right] < target:  # 타겟보다 작으면 왼쪽 포인터 +1
                left += 1
            elif nums_s[left] + nums_s[right] > target: # 타겟보다 크면 오른쪽 포인터 -1
                right -= 1
            else:                                       # 같으면 멈춤
                break
        if nums_s[left] == nums_s[right]:               # 값이 같은 경우에 [3,2,3]
            left_ = nums.index(nums_s[left])            # 처음 나오는 값의 인덱스를 left_에 담고
            nums[left_] = '*'                           # 또 발견되면 안되니까 *로 바꿔주고 [*, 2, 3]
            right_ = nums.index(nums_s[right])          # 두번째 나오는 값의 인덱스를 right_에 담음
        else:
            left_ = nums.index(nums_s[left])            # 값이 같은 경우가 아닌 경우라면 *로 안 바꿔주고 그냥 담으면 됨
            right_ = nums.index(nums_s[right])
        return [left_, right_]


# nums = [2,7,11,15]
# target = 9
nums = [3,2,3]
target = 6



sol = Solution()
print(sol.twoSum(nums, target))