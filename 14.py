from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):

            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
                
            res += strs[0][i]

        return res
    
if __name__ == "__main__":
    sol = Solution()

    #Exmaple 1
    strs  = ["flowers", "flow", "flight"]
    print(sol.longestCommonPrefix(strs))

    #Example 2
    strs2 = ["dog","racecar","car"]
    print(sol.longestCommonPrefix(strs2))