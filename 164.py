from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()

        if len(nums) < 2:
            return 0

        max_gap=0

        for i in range(len(nums)-1):
            gap = nums[i+1] - nums[i]

            if  max_gap < gap :
                max_gap=gap
            
        return max_gap

sol = Solution()

nums1 = [3,6,9,1]
nums2 = [10]

print(sol.maximumGap(nums1))
print(sol.maximumGap(nums2))