from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return res

sol = Solution()

print(sol.subsets([1,2,3]))
#Expected Output : [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

print(sol.subsets([0]))
#Expected Output : [[],[0]]
