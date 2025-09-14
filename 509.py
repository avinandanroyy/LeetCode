class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        prev, cur = 0, 1

        for i in range(2, n + 1):
            prev, cur = cur, prev + cur

        return cur
    
if __name__ == "__main__":
    sol = Solution()

    n1, n2, n3 = 2, 3, 4

    print(sol.fib(n1))
    print(sol.fib(n2))
    print(sol.fib(n3))

    print(sol.fib(5))