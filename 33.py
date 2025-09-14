from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        left, right = 0, len(nums) - 1

        # Find the smallest element (pivot)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        pivot = left
        left, right = 0, len(nums) - 1

        # Decide which side to search
        if nums[pivot] <= target <= nums[right]:
            left = pivot
        else:
            right = pivot - 1

        # Binary search
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
    
if __name__ == "__main__":
    sol = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(sol.search(nums, target))   # Output: 4
