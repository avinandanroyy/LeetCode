import heapq
from typing import List

class Solution:
    def findKthlargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)

            if len(min_heap) > k :
                heapq.heappop(min_heap)

        return min_heap[0]

sol = Solution()
#Example One 
nums1 = [3,2,1,5,6,4]
k1 = 2

print(sol.findKthlargest(nums1,k1)) #Expected Output : 5

#Example Two
nums2 = [3,2,3,1,2,4,5,5,6]
k2 = 4

print(sol.findKthlargest(nums2,k2)) #Expected Output : 4