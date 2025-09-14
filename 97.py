class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, k = len(s1), len(s2), len(s3)

        if n + m != k:
            return False

        dp = [[False] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i - 1]
                else:
                    from_s1 = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                    from_s2 = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                    dp[i][j] = from_s1 or from_s2

        return dp[n][m]


sol = Solution()

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(sol.isInterleave(s1,s2,s3))