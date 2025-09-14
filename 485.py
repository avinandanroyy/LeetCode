from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxcount = 0
        for i in nums:
            if i == 1:
                count += 1
                if count > maxcount:
                    maxcount = count
            else:
                count =0
        return maxcount
    

if __name__ == "__main__":
    sol = Solution()

    nums1 = [1,1,0,1,1,1]
    nums2 = [1,0,1,1,0,1]

    print(sol.findMaxConsecutiveOnes(nums1))
    print(sol.findMaxConsecutiveOnes(nums2))
