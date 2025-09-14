from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        totalJumps = 0
        destination = len(nums) - 1
        coverage = 0
        lastJumpIdx = 0

        if len(nums) == 1:
            return 0

        for i in range(len(nums)):
            coverage = max(coverage, i + nums[i])

            if i == lastJumpIdx:
                lastJumpIdx = coverage
                totalJumps += 1

                if coverage >= destination:
                    return totalJumps

        return totalJumps

sol = Solution()

nums = [2,3,1,1,4]
arr = [2,3,0,1,4]

print(sol.jump(nums))
#Expected Output : 2

print(sol.jump(arr))
#Expected Output : 2