from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        maxLength = 1
        incLength = 1
        decLength = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                incLength += 1
                decLength = 1
            elif nums[i] < nums[i - 1]:
                decLength += 1
                incLength = 1
            else:
                incLength = 1
                decLength = 1

            maxLength = max(maxLength, incLength, decLength)

        return maxLength
    
sol = Solution()

print(sol.longestMonotonicSubarray([1,4,3,3,2])) #Expected Output :  2
print(sol.longestMonotonicSubarray([3,3,3,3])) #Expected Output : 1
print(sol.longestMonotonicSubarray([3,2,1])) #Expected Output : 3