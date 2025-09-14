from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range(2 * n):
            num = nums[i % n]

            while stack and nums[stack[-1]] < num:
                result[stack.pop()] = num

            if i < n:
                stack.append(i)

        return result

sol = Solution()
nums = [1, 2, 1]
print(sol.nextGreaterElements(nums))
# Output: [2, -1, 2]