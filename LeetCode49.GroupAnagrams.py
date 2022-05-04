from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_edit = strs                    # 원본이 바뀌면 안되므로 복사본 새로 담아줌
        strs_srt = []                       # sort한 문자열들을 담아줄 리스트
        ans = []
        for i in range(len(strs)):          # 각 문자열 마다 sort
            strs_srt.append((''.join(sorted(strs_edit[i]))))    # sort한 문자열을 담음
        print(strs_srt)
        strs_uni = list(set(strs_srt))  # sort한 문자열의 unique한 값을 리스트에 담음
        print(strs_uni)
        for j in range(len(strs_uni)):          # unique한 값만 담은 리스트를 순차적으로 돌면서
            tmp = []
            for k in range(len(strs)):          
                if strs_uni[j] == strs_srt[k]:  # unique한 값과 소팅된 값이 같을 때에만 
                    tmp.append(strs[k])         # tmp 리스트에 담고
            ans.append(tmp)                     # 다시 정답리스트에 넣어서 이중 리스트를 만들어줌

        return ans                              

strs = ["eat","tea","tan","ate","nat","bat"]
# strs = [""]
# strs = ["a"]
sol = Solution()
print(sol.groupAnagrams(strs))






        
        