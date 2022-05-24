
# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         for i in range(len(logs)):
#             logs_list = []
#             tmp = logs[i].split()
#             tmp = [tmp[0], tmp[1:]]
#             logs_list.append(tmp)

#         sorted(logs_list, key = lambda x:(x[1], x[0]))

# 이중리스트 정렬 기준을 모르겠어서 답을 봄




# point : 숫자로 시작되는 로그는 정렬을 하지 않는다.
from typing import List
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        nums, char = [], []
        for i in range(len(logs)):              # [0]은 식별자이므로 1로 판별
            if logs[i].split()[1].isdigit():    # 숫자일때 num에 넣고
                nums.append(logs[i])
            else:
                char.append(logs[i])            # 그외 문자열은 char에 넣음

        char.sort(key = lambda x:(x.split()[1:], x.split()[0])) # 문자열 담은 것만 sort
    
        return char + nums  # 숫자로 시작되는 로그는 그냥 원래 순서대로 넣으면 됨

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
sol = Solution()
print(sol.reorderLogFiles(logs))