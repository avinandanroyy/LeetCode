from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result ^= num
            
        return result

    
if __name__ == "__main__":
    nums = [2,2,1]
    k = [4,1,2,1,2]
    x = [1]

    sol = Solution()

    print(sol.singleNumber(nums))
    print(sol.singleNumber(k))
    print(sol.singleNumber(x))
