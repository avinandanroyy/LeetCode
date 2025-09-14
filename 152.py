from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        global_max = nums[0]
        current_max = nums[0]
        current_min = nums[0]


        for i in range(1, len(nums)):
            num = nums[i]
            temp_max = current_max
            current_max = max(num, num * temp_max, num * current_min)
            current_min = min(num, num * temp_max, num * current_min)
            global_max = max(global_max, current_max)

        return global_max

output1 = Solution().maxProduct([2,3,-2,4])
output2 = Solution().maxProduct([-2,0,-1])

print(output1)
print(output2)


        