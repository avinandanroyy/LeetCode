from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(open_n: int, close_n: int, path: List[str], res: List[str]):
            if open_n == close_n == n:
                res.append("".join(path))
                return
            
            if open_n < n:
                path.append("(")
                backtrack(open_n + 1, close_n, path, res)
                path.pop()
            
            if close_n < open_n:
                path.append(")")
                backtrack(open_n, close_n + 1, path, res)
                path.pop()
        
        result = []
        backtrack(0, 0, [], result)
        return result
    
if __name__ == "__main__":

    n = 3
    m = 1

    sol = Solution()

    print(sol.generateParenthesis(n))
    print(sol.generateParenthesis(m))