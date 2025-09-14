from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand, count = 0, 0

        for i in range(0,len(nums)):

            if count == 0:
                cand = nums[i]
            
            if cand == nums[i]:
                count += 1
            else:
                count -= 1
        
        return cand

if __name__ == "__main__":
    nums = [3,2,3]
    nums1 = [2,2,1,1,1,2,2]

    sol = Solution()

    print(sol.majorityElement(nums))
    print(sol.majorityElement(nums1))
            