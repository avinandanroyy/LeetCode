from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x  = len(nums)

        for i in range(len(nums)):
            x = x ^ i ^ nums[i]

        return x

if __name__ == "__main__":
    sol = Solution()

    nums1 = [3,0,1]
    nums2 = [0,1]
    nums3 = [9,6,4,2,3,5,7,0,1]

    print(sol.missingNumber(nums1))
    print(sol.missingNumber(nums2))
    print(sol.missingNumber(nums3))
