class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        mp = 0 
        for r in range(len(prices)) : 
            if prices[l] < prices[r] : 
                profit = prices[r] - prices[l]
                mp = max(profit, mp)  
            else : 
                l = r
        return mp
                