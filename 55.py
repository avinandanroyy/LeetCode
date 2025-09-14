from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastpos = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= lastpos:
                lastpos = i

        return lastpos == 0
    

sol = Solution()

print(sol.canJump([2,3,1,1,4])) #True
print(sol.canJump([3,2,1,0,4])) #False
