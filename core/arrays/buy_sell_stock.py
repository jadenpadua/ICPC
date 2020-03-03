class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        maxProfit = 0
        minPrice = prices[0]
        for price in prices:
            #Updates min price if a number in the array is smaller
            minPrice = min(minPrice,price)
            #calculates our current profit from the min price anchor
            currentProfit = price - minPrice
            #calculates max profit between current profit and prev max 
            maxProfit = max(currentProfit,maxProfit)
        return maxProfit
#O(n) time | O(1)
