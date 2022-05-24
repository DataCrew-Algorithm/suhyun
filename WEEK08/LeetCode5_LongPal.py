class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        if len(s) == 1:
            return s

        else:
        
            for diff in range(len(s)-1, 0, -1):
                start = 0
                end = diff - start
                
                # print(diff)
                while end != len(s)+1:
                    tmp = s[start:end+1]

                    if tmp == tmp[::-1]:
                        
                        ans = tmp
                        # print(ans)
                        break
                    else:
                        start += 1
                        end += 1
                if ans:
                    break

            return ans
# s = "bb"
s = "vnjwvalrbypfcbqnmopltjnoifmzwgvpzqzsdtvawndpjtpmpjbjionjifqtvvocpeaftvhpdgjjfafunfndztdjkcxyihtsyppendfzzjeyxlbwpdygiqmdqcdbmgyjigrmfkswcwryaydjilqqxvcnyvviesuncslvzikawwqykqwdfibggezufqihcjkebapmgkvwixywgdextafxycnipjglsndkyjoqfyfljfkkvoieksmavdlmlhhnstesibffiopqvlyuidvrawndbzonwzbsjmpeqoglmdbinkovqpzfkxihzitdopnomseqhmrrkcsvrzziphwpuhjngeotwcrebcmbtirkgeavojtmpakcewmexhxacngknokxsvtqobdgckutpexswgwqzbosjpxauyflnylfcxsucsehqvakbpvfmkelmkspsqxnutwfwacpqqvovdqafeylobneojdsgqowcbxfsvuqusdbylcgcvgrofgvzubakjmlbffjhrafvnqttwuyhokzpmhlludpbowuxzrebxsdusalljfjgjkucwzpmndqncykvfnbrxcrcaxwisjpstejjqbpwegpxyrtyafxklgralnkwxkmjpuqfixzkonznmguyizlancpxdzcfkgiotyelegprbaytdhbutbuihkxnbtuqrtezaskfqsmrznfohhlqp"
sol = Solution()
print(sol.longestPalindrome(s))


# 리스트 이용


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         ans = ''
#         if len(s) == 1:
#             return s

#         else:
        
#             for diff in range(len(s)-1, 0, -1):
#                 start = 0
#                 end = diff - start
                
#                 # print(diff)
#                 while end != len(s)+1:
#                     s_ = list(s)
#                     s_ = list(reversed(s_[start:end+1]))
#                     # print(s_)
#                     if list(s[start:end+1]) == s_:
#                         # print(list(s[start:end+1]))
#                         # print(s[start:end+1])
#                         ans = s[start:end+1]
#                         # print(ans)
#                         break
#                     else:
#                         start += 1
#                         end += 1
#                 if ans:
#                     break

#             return ans
# s = "bb"
# sol = Solution()
# print(sol.longestPalindrome(s))