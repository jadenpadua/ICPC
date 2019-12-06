class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        maxProfit = 0
        minPrice = prices[0]
        
        for price in prices:
            minPrice = min(minPrice,price)
            currentProfit = price - minPrice
            maxProfit = max(currentProfit,maxProfit)
        return maxProfit
