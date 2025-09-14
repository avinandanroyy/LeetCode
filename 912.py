'''
Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in 
functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
'''

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def heapify(n: int, i: int):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and nums[left] > nums[largest]:
                largest = left

            if right < n and nums[right] > nums[largest]:
                largest = right

            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(n, largest)

        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(i, 0)

        return nums
    
sol = Solution()

print(sol.sortArray([5,2,3,1]))
print(sol.sortArray([5,1,1,2,0,0]))
