class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        res = 0
        r = 0

        for i in range(1,n):
            if word[i] == word[i-1]:
                r += 1
            else:
                res += r
                r = 0
        return res+r+1
    
if __name__ == "__main__":
    sol = Solution()

    word = "abbcccc"
    print(sol.possibleStringCount(word))