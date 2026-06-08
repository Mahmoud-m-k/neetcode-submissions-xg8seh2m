class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = 0
        profit = 0
        l, r  = 0, 1
        #l is buy r is sell
        while r < len(prices):
            if prices[l] < prices[r]:
                highest = prices[r] - prices[l]
                profit = max(highest, profit)
                r += 1
            else:
                l = r
                r = l + 1

            
                
            
        return profit
        