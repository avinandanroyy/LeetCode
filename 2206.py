from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        odd_set = set()

        for n in nums:
            if n not in odd_set:
                odd_set.add(n)
            else:
                odd_set.remove(n)

        return len(odd_set) == 0