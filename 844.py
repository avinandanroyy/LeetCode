class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def buildStack(string: str) -> list:
            stack = []
            for c in string:
                if c == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return stack

        return buildStack(s) == buildStack(t)
    
sol = Solution()

print(sol.backspaceCompare("ab#c","ad#c"))
print(sol.backspaceCompare("ab##","c#d#"))
print(sol.backspaceCompare("a#c","b"))