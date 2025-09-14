class Solution:
    def climbStairs(self, n: int) -> int:
        one , two = 1, 1
        
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        
        return one
    
if __name__ == "__main__":
    sol = Solution()

    n = 2
    y = 3

    print(sol.climbStairs(n))
    print(sol.climbStairs(y))