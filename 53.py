from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum, sum = nums[0], 0

        for i in range(len(nums)):
            sum += nums[i]

            if sum > maxsum:
                maxsum = sum
            
            if sum < 0:
                sum = 0
        
        return maxsum
    
if __name__ == "__main__":
    sol = Solution()

    nums1 = [-2,1,-3,4,-1,2,1,-5,4]
    nums2 = [1]
    nums3 = [5,4,-1,7,8]

    print(sol.maxSubArray(nums1))
    print(sol.maxSubArray(nums2))
    print(sol.maxSubArray(nums3))