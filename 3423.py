from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        max_diff = 0
        for i in range(n):
            diff = abs(nums[i] - nums[(i+1) % n])
            max_diff = max(max_diff, diff)
        return max_diff
    
if __name__ == "__main__":
    sol = Solution()

    print(sol.maxAdjacentDistance([1,2,4]))
    print(sol.maxAdjacentDistance([-5,-10,-5]))