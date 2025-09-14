'''
Given an integer array nums, return an array answer such that answer[i] is 
equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
'''

# For Example 
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n

        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]
        right_product = 1
        
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result

sol = Solution()
nums = [1,2,3,4]
print(sol.productExceptSelf(nums))  
arr = [-1,1,0,-3,3]
print(sol.productExceptSelf(arr))
