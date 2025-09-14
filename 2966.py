from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        if n % 3 != 0:
            return []
        
        nums.sort()
        
        result = []

        for i in range(0, n, 3):
            group = nums[i: i+3]

            if group[2] - group[0] > k:
                return []

            result.append(group)
        
        return result
        
if __name__ == "__main__":
    sol = Solution()

    nums = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11]
    k = 14

    print(sol.divideArray([1,3,4,8,7,9,3,5,1],2))
    print(sol.divideArray([2,4,2,2,5,2],2))
    print(sol.divideArray(nums,k))