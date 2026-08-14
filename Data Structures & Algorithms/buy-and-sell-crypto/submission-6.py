class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        mp = 0
        for r in range(len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                mp = max(profit, mp)
            else :
                l = r
        return mp 