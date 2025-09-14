from typing import List

class Solution:
    def _rob_linear(self, arr: List[int]) -> int:
        rob, cool = 0, 0
        
        for num in arr:
            rob, cool = cool + num, max(rob, cool)
            
        return max(rob, cool)

    def rob(self, nums: List[int]) -> int:
       
        if len(nums) <= 1:
            return nums[0] if nums else 0

    
        max_excluding_last = self._rob_linear(nums[:-1])
        
       
        max_excluding_first = self._rob_linear(nums[1:])

        return max(max_excluding_last, max_excluding_first)


print(Solution().rob([2,3,2]))
print(Solution().rob([1,2,3,1]))
print(Solution().rob([1,2,3]))