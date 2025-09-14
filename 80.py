from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 0 

        for num in nums:
            if k < 2 or num != nums[k - 2]:
                nums[k] = num
                k += 1

        return k

sol = Solution()

#Example 1
nums1 = [1,1,1,2,2,3]
print(sol.removeDuplicates(nums1), ",nums = ",nums1)
#Expected Output : 5 ,nums =  [1, 1, 2, 2, 3, 3]


#Example 2
nums2 = [0,0,1,1,1,1,2,3,3]
print(sol.removeDuplicates(nums2),",nums = ",nums2)
#Expected Output : 7 ,nums =  [0, 0, 1, 1, 2, 3, 3, 3, 3]