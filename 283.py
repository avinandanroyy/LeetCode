from typing import List

class Solution:
    def moveZeros(self, nums: List[int]) -> List[int]:
        l = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1

        return nums

if __name__ == "__main__":
    sol = Solution()

    nums = [0,1,0,3,12]
    r = [0]
    arr = [1,2,0,34,54,0,0,34534,67,0]
    print(sol.moveZeros(nums))
    print(sol.moveZeros(r))
    print(sol.moveZeros(arr))
