from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        
        # Two pointers for positive and negative indices
        pos_index = 0
        neg_index = 1
        
        # Single pass through the array
        for num in nums:
            if num > 0:
                result[pos_index] = num
                pos_index += 2
            else:
                result[neg_index] = num
                neg_index += 2
        
        return result

if __name__ == "__main__":
    sol = Solution()

    print(sol.rearrangeArray([3,1,-2,-5,2,-4]))
    print(sol.rearrangeArray([-1,1]))