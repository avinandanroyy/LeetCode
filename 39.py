from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start: int, current: List[int], target: int):
            if target == 0:
                result.append(list(current))
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, target - candidates[i])
                current.pop()
        
        backtrack(0, [], target)
        return result
    
sol = Solution()

candidates = [2,3,6,7]
target = 7
candidates1 = [2,3,5]
target1 = 8

print(sol.combinationSum(candidates,target)) 
#Expected Output : [[2,2,3],[7]]

print(sol.combinationSum(candidates1,target1))
#Expected Output : [[2,2,2,2],[2,3,3],[3,5]]

print(sol.combinationSum([2],1))
#Expected Output : []