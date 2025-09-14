from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for i in range(1,len(prices)):

            if prices[i] < buy_price:
                buy_price = prices[i]
            else:
                current_profit = prices[i] - buy_price
                profit = max(current_profit, profit)

        return profit
    
if __name__ == "__main__":
    sol = Solution()

    prices = [7,1,5,3,6,4]
    stocks = [7,6,4,3,1]

    print(sol.maxProfit(prices))
    print(sol.maxProfit(stocks))