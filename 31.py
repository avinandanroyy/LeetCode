from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> List[int]:
        pivot = None
        
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pivot = i - 1
                break

        else:
            nums.reverse()
            return
            
        swap = len(nums) - 1

        while nums[swap] <= nums[pivot]:
            swap -= 1

        nums[pivot], nums[swap] = nums[swap], nums[pivot]

        nums[pivot + 1:] = reversed(nums[pivot + 1:])

        return nums
    
if __name__ == "__main__":
    sol = Solution()

    nums1 = [1,2,3]
    nums2 = [3,2,1]
    nums3 = [1,1,5]

    print(sol.nextPermutation(nums1))
    print(sol.nextPermutation(nums2))
    print(sol.nextPermutation(nums3))