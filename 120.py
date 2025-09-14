from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        for i in range(n -2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0][0]

sol = Solution()

#method 1 to call a function
triangle1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
res = Solution().minimumTotal(triangle1)
print(res)

#method 2 to call a function
triangle2 = [[-10]]
print(Solution().minimumTotal(triangle2))

#method 3 to call a function
triangle3 = [[-1],[-2,-3],[-1,-5,-1]]
print(sol.minimumTotal(triangle3))

#method 4 to call a function
if __name__ == "__main__":
    sol = Solution()
    triangle4 = [[-1],[2,3],[1,-1,-3]]
    print(sol.minimumTotal(triangle4))