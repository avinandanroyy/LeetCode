class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split("/")
        stack = []

        for component in components:
            if component == "" or component == ".":
                continue
            elif component == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(component)

        result = "/" + "/".join(stack)
        return result
    
sol = Solution()
print(sol.simplifyPath("/home/"))
print(sol.simplifyPath("/home//foo/"))
print(sol.simplifyPath("/home/user/Documents/../Pictures"))
print(sol.simplifyPath("/../"))
print(sol.simplifyPath("/.../a/../b/c/../d/./"))