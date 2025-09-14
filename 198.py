from typing import List

class Solution:
    def rob(self, nums: list[int]) -> int:
        rob_one_step_ago = 0
        rob_two_steps_ago = 0
        for num in nums:
            current_max = max(num + rob_two_steps_ago, rob_one_step_ago)
            rob_two_steps_ago = rob_one_step_ago
            rob_one_step_ago = current_max

        return rob_one_step_ago


print(Solution().rob([1,2,3,1]))
print(Solution().rob([2,7,9,3,1]))