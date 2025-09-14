from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        n = len(nums)
        return [num for num, count in freq.items() if count > n // 3]
        
    
if __name__ == "__main__":
    sol = Solution()

    nums1 = [3,2,3]
    nums2 = [1]
    nums3 = [1,2]
    nums4 = [1,1,1,2,2,2,3]
    
    print(sol.majorityElement(nums1))
    print(sol.majorityElement(nums2))
    print(sol.majorityElement(nums3)) 
    print(sol.majorityElement(nums4)) 