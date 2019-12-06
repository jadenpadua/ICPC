class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                currentProfit = prices[j] - prices[i]
                if currentProfit > 0:
                    if currentProfit > maxProfit:
                        maxProfit = currentProfit
        return maxProfit
