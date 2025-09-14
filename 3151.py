from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                return False
        return True
    
sol = Solution()

print(sol.isArraySpecial([1])) #Expected Output : True
print(sol.isArraySpecial([2,1,4])) #Expected Output : True
print(sol.isArraySpecial([4,3,1,6])) #Expectde Output : False