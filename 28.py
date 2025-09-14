class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        len_hay, len_ndl = len(haystack) , len(needle)

        for i in range(len_hay - len_ndl + 1):
            if haystack[i:i + len_ndl] == needle:
                return i
            
        return -1
    
if __name__ == "__main__":
    sol = Solution()

    #Example 1
    haystack , needle = "sadbutsad" , "sad"
    print(sol.strStr(haystack, needle))

    #Example 2
    haystack1 , needle1 = "leetcode" , "leeto"
    print(sol.strStr(haystack1,needle1))