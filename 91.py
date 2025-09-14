class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  
        dp[1] = 1  
    
        for i in range(2, n + 1):
            
            current_char = s[i-1]
            if current_char != '0':
                dp[i] += dp[i-1]
        
        
            two_chars = s[i-2:i]
            if two_chars[0] != '0' and int(two_chars) <= 26:
                dp[i] += dp[i-2]
    
        return dp[n]

sol = Solution()

print(sol.numDecodings("12"))
print(sol.numDecodings("226"))
print(sol.numDecodings("06"))