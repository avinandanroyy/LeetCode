from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            first = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    first = mid
                    right = mid - 1  # Continue searching in left half
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return first
        
        def findLast(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            last = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    last = mid
                    left = mid + 1  # Continue searching in right half
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return last
        
        return [findFirst(nums, target), findLast(nums, target)]
    
if __name__ == "__main__":
    sol = Solution()

    nums1 = [5,7,7,8,8,10]
    target1 = 8

    nums2, target2 = [5,7,7,8,8,10], 6

    nums3, target3 = [], 9

    print(sol.searchRange(nums1,target1))
    print(sol.searchRange(nums2,target2))
    print(sol.searchRange(nums3,target3))