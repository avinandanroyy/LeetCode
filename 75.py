from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        i = 0

        def swap(i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i <= right:
            if nums[i] == 0:
                swap(left,i)
                left += 1

            elif nums[i] == 2:
                swap(i,right)
                right -= 1
                i -= 1
            
            i += 1
        
        return nums
    
if __name__ == "__main__":
    sol = Solution()

    nums1 = [2,0,2,1,1,0]
    nums2 = [2,0,1]

    print(sol.sortColors(nums1))
    print(sol.sortColors(nums2))