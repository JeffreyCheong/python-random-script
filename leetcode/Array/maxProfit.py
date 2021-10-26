
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        profit = 0
        cheapest = prices[0]

        for i in range(1, len(prices)):
            if cheapest > prices[i]:
                cheapest = prices[i]

            else:
                profit = max(prices[i] - cheapest, profit)

        return profit


if __name__ == '__main__':

    prices = [7,1,5,3,6,4]
    
    sol = Solution()

    answer = sol.maxProfit(prices=prices)

    print(answer)