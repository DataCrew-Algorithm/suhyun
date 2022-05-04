from typing import List
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        para_l = re.sub(r'[^\w\s]', ' ', paragraph) # \w 단어 문자, \s 공백 -> ' '공백으로 바꿔줌
        para_l = para_l.lower().split()
        print(para_l)
        para_uni = list(set(para_l))    # set으로 바꿔줘서 중복 되는 것을 없애줌
        print(para_uni)
        num = 0                         # 0개라고 초기값으로 둠
        ans = para_uni[0]               # 첫 단어를 초기값으로
        for word in para_uni:
            if word not in banned:
                c = para_l.count(word)
                if c > num:             # 새로운 단에에 대해 count한 숫자가 원래있던 숫자보다 크면, 
                    num = c             
                    ans = word          # 불러왔단 문자열을 정답에 담는다.
            

        return ans

# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
paragraph ="a, a, a, a, b,b,b,c, c"
banned =["a"]
# paragraph = "a."
# banned = []
sol = Solution()
print(sol.mostCommonWord(paragraph, banned))
                
            
