from typing import List
from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        center = False
        res = 0
        c = Counter(words)

        for word, freq in c.items():
            rev = word[::-1]

            if word[0] == word[1]: # like 'gg'
                res += (c[word] // 2) * 4
                if c[word] % 2:
                    center = True
                
            else:
                if word[::-1] in c: # 'lc cl'
                    res += min(freq, c[rev]) * 2
        return res + (center * 2)
    
sol = Solution()
print(sol.longestPalindrome(["lc","cl","gg"]))  # Output: 6
print(sol.longestPalindrome(["ab","ty","yt","lc","cl","ab"]))  # Output: 8
