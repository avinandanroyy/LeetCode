class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_counts = [0] * 128

        for c in s:
            char_counts[ord(c)] += 1

        result = 0
        for count in char_counts:
            result += (count // 2) * 2
            if result % 2 == 0 and count % 2 == 1:
                result += 1

        return result
    
    
sol = Solution()
print(sol.longestPalindrome("abccccdd"))  # Output: 7
print(sol.longestPalindrome("a"))         # Output: 1
print(sol.longestPalindrome("bb"))        # Output: 2