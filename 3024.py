from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if (nums[0] + nums[1] <= nums[2] or
            nums[0] + nums[2] <= nums[1] or
            nums[1] + nums[2] <= nums[0]):
            return "none"
        
        if nums[0] == nums[1] and nums[1] == nums[2]:
            return "equilateral"
        
        if nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
            return "isosceles"
        
        return "scalene"

sol = Solution()
print(sol.triangleType([3, 3, 3]))    # Output: equilateral
print(sol.triangleType([3, 4, 5]))    # Output: scalene
print(sol.triangleType([3, 3, 5]))    # Output: isosceles
print(sol.triangleType([1, 2, 3]))    # Output: none
