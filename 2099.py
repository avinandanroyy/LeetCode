from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed_nums = [(nums[i], i) for i in range(len(nums))]
        indexed_nums.sort(key=lambda x: x[0], reverse=True)
        k_largest = indexed_nums[:k]
        k_largest.sort(key=lambda x: x[1])
        result = [num for num, _ in k_largest]
        return result
    
if __name__ == "__main__":
    sol = Solution()

    nums1 = [2,1,3,3]
    k1 = 2
    nums2 = [-1,-2,3,4]
    k2 = 3
    nums3 = [3,4,3,3]
    k3 = 2

    print(sol.maxSubsequence(nums1,k1))
    print(sol.maxSubsequence(nums2,k2))
    print(sol.maxSubsequence(nums3,k3))