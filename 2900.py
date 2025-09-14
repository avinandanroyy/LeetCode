class Solution:
    def getLongestSubsequence(self, words, groups):
        res=[words[0]]
        prev=groups[0]
        for i in range(1,len(words)):
            if groups[i]!=prev:
                res.append(words[i])
                prev=groups[i]
        return res
sol = Solution()
words = ["apple", "banana", "cherry", "date", "elderberry"]
groups = [1, 2, 1, 2, 1]

print(sol.getLongestSubsequence(words, groups))
# Expected output: ['apple', 'banana', 'cherry', 'date', 'elderberry']
