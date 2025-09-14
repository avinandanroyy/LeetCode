from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        prem = []
        count = { n:0 for n in nums}
        for n in nums:
            count[n] += 1
        
        def dfs():
            if len(prem) == len(nums):
                res.append(prem.copy())
                return
            
            for n in count:
                if count[n] >  0:
                    prem.append(n)
                    count[n] -= 1

                    dfs()

                    count[n] +=  1
                    prem.pop()

        dfs()
        return res
    
if __name__ == "__main__":
    nums = [1,1,2]
    nums1 = [1,2,3]

    sol = Solution()

    print(sol.permuteUnique(nums))
    print(sol.permuteUnique(nums1))