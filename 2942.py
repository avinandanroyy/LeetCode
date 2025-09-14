class Solution:
    def findWordsContaining(self, words, x):
        result = []
        
        for i in range(len(words)):
            if x in words[i]:
                result.append(i)
        
        return result

sol = Solution()
words = ["apple", "banana", "cherry", "date"]
x = "a"
print(sol.findWordsContaining(words, x))
# Output: [0, 1, 3]
