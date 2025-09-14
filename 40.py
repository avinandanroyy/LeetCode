from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def backtrack(start: int, current: List[int], target: int):
            if target == 0:
                result.append(list(current))
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                current.append(candidates[i])
                backtrack(i + 1, current, target - candidates[i])
                current.pop()
        
        backtrack(0, [], target)
        return result
    
sol = Solution()

candidates = [10,1,2,7,6,1,5]
target = 8
print(sol.combinationSum2(candidates,target))
'''
Expected Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
'''

print(sol.combinationSum2([2,5,2,1,2],5))
'''
Expected Output: 
[
[1,2,2],
[5]
]
'''
