class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(" , "]" : "[",  "}": "{"}

        for c in s :
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()

                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

if __name__ == "__main__":
    sol = Solution()

    #Example 1
    s = "()"
    print(sol.isValid(s))

    #Example 2
    r = "()[]{}"
    print(sol.isValid(r))

    #Example 3
    t = "(]"
    print(sol.isValid(t))

    #Example 4
    u  = "([])"
    print(sol.isValid(u))