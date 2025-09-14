from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
                
        return max_profit


solver = Solution()
print(solver.maxProfit([7,1,5,3,6,4]))
print(solver.maxProfit([1,2,3,4,5]))
print(solver.maxProfit([7,6,4,3,1]))