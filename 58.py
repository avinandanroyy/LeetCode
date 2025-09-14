class Solution:
    def lengthofLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0

        while s[i] == " ":
            i -= 1

        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length
    
if __name__ == "__main":
    sol =Solution()

    #Example 1
    s = "Hello World"
    print(sol.lengthofLastWord(s))

    #Example 2
    t = "   fly me   to   the moon  "
    print(sol.lengthofLastWord(t))

    #Example 3
    u = "luffy is still joyboy"
    print(sol.lengthofLastWord(u))