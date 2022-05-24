class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = [i for i in s if i.isalnum()]
        new_str = ''.join(new_str)
        new_str = new_str.lower()


        if new_str == new_str[::-1]:
            return True

        else:
            return False

sol = Solution()
print(sol.isPalindrome("0P"))