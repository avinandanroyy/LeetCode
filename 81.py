from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return True
            
            # Handle duplicates: if left, mid, and right are all equal
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue
            
            # Left part is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right part is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False
        
sol = Solution()

#Example 1
nums1 = [2,5,6,0,0,1,2]
target1 = 0
print(sol.search(nums1, target1)) #Expected Output : true

#Example 2
nums2 = [2,5,6,0,0,1,2]
target2 = 3
print(sol.search(nums2,target2)) #Expected Output : false