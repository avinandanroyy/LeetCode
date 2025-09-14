from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_val = nums[0]
        max_val = nums[0]
        res = 1
        for num in nums:
            if num - min_val > k:
                res +=1
                min_val = num
        return res
    
sol = Solution()

print(sol.partitionArray([3,6,1,2,5],2)) #Expected Output : 2
print(sol.partitionArray([1,2,3],1)) #Expected Output : 2
print(sol.partitionArray([2,2,4,5],0)) #Expected Ouptut : 3