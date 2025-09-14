from typing import List
import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> int:
        strs = [str(num) for num in nums]

        def compare(s1, s2):
            if s1 + s2 > s2 + s1:
                return -1  
            else:
                return 1   
            
        sorted_strs = sorted(strs, key=functools.cmp_to_key(compare))
    
    
        result = "".join(sorted_strs)
    
        if result[0] == '0':
            return "0"
        else:
            return result


sol = Solution()

print(sol.largestNumber([10,2]))