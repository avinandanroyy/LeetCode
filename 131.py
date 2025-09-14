from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        
        def backtrack(start: int, path: List[str], result: List[List[str]]):
        
            if start == len(s):
                result.append(path[:])
                return
            
           
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    
                    path.append(substring)
                    backtrack(end, path, result)
                    path.pop() 
        
        result = []
        backtrack(0, [], result)
        return result 

if __name__ == "__main__":
    sol = Solution()

    print(sol.partition("aab"))
    print(sol.partition("a"))