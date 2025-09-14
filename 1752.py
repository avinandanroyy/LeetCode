from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        c = 0

        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                c+=1 #increasig order 0 or shift 1
        if nums[len(nums)-1] > nums[0]:
            c+=1 
        return c<=1
        
if __name__ == "__main__":
    sol = Solution()

    nums1 = [3,4,5,1,2]
    nums2 = [2,1,3,4]
    nums3 = [1,2,3]

    print(sol.check(nums1))
    print(sol.check(nums2))
    print(sol.check(nums3))

#Time Complexity  = O(n)
#Space Complexity = O(1)