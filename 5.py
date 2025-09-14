class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        LPS = ""

        for i in range(1, len(s)):
            # Odd length palindrome
            low = i
            high = i
            while low >= 0 and high < len(s) and s[low] == s[high]:
                low -= 1
                high += 1
            palindrome = s[low + 1:high]
            if len(palindrome) > len(LPS):
                LPS = palindrome

            # Even length palindrome
            low = i - 1
            high = i
            while low >= 0 and high < len(s) and s[low] == s[high]:
                low -= 1
                high += 1
            palindrome = s[low + 1:high]
            if len(palindrome) > len(LPS):
                LPS = palindrome

        return LPS

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("babad"))  # "bab" or "aba"
    print(sol.longestPalindrome("cbbd"))   # "bb"
