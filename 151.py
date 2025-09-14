class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join(words[::-1])
    
sol  = Solution()

s = "the sky is blue"
print(sol.reverseWords(s))
#Expected Output : "blue is sky the"

x = "  hello world  "
print(sol.reverseWords(x))
#Expected Output : "world hello"

y = "a good   example"
print(sol.reverseWords(y))
#Expected Output : "example good a"