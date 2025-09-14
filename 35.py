from typing import List

class Solution:
    def insertPosition(self, nums: List[int], target: int) -> int:
        start , end = 0 , len(nums)

        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return start

if __name__ == "__main__":
    sol = Solution()

    #Eaxmple 1
    nums, target = [1,3,5,6] , 5
    print(sol.insertPosition(nums,target))

    #Example 2
    nums1, target1 = [1,3,5,6], 2
    print(sol.insertPosition(nums1,target1))

    #Example 3
    nums2, target2 = [1,3,5,6], 7
    print(sol.insertPosition(nums2,target2))