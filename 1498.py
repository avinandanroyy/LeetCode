from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        
        n = len(nums)
        left, right = 0, n - 1
        result = 0
        
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i-1] * 2) % MOD
        
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                result = (result + pow2[right - left]) % MOD
                left += 1
        
        return result 
    
if __name__ == "__main__":
    sol = Solution()

    nums1, target1 = [3,5,6,7], 9
    nums2, target2 = [3,3,6,8], 10
    nums3, target3 = [2,3,3,4,6,7], 12

    print(sol.numSubseq(nums1,target1))
    print(sol.numSubseq(nums2,target2))
    print(sol.numSubseq(nums3,target3))