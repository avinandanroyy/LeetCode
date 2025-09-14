from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

sol = Solution()

nums1 = [1,2,3,1]
print(sol.containsDuplicate(nums1))

nums2 = [1,2,3,4]
print(sol.containsDuplicate(nums2))

nums3 = [1,1,1,3,3,4,3,2,4,2]
print(sol.containsDuplicate(nums3))