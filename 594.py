from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        longest = 0
        
        for num in cnt:
            if num + 1 in cnt:
                current = cnt[num] + cnt[num + 1]
                if current > longest:
                    longest = current
        
        return longest

if __name__ == "__main__":
    sol = Solution()

    nums = [1,3,2,2,5,2,3,7]
    nums2 = [1,2,3,4]
    nums3 = [1,1,1,1]

    print(sol.findLHS(nums))
    print(sol.findLHS(nums2))
    print(sol.findLHS(nums3))