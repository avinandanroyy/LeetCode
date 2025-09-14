from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        word_set = set(wordDict)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):

                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]

sol = Solution()
s = "leetcode"
wordDict = ["leet","code"]
print(sol.wordBreak(s,wordDict))

s1 = "applepenapple"
wordDict1 = ["apple","pen"]

s2 = "catsandog"
wordDict2 = ["cats","dog","sand","and","cat"]

print(sol.wordBreak(s1,wordDict1))
print(sol.wordBreak(s2,wordDict2))