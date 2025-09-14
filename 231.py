class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 1
        while x < n:
            x *= 2
        return x == n
    
if __name__ == "__main__":
    sol = Solution()

    n = 1
    n1 = 16
    n2 = 3

    print(sol.isPowerOfTwo(n))
    print(sol.isPowerOfTwo(n1))
    print(sol.isPowerOfTwo(n2))