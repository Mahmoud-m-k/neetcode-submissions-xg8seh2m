class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = 0
        s = 0
        

        for i in range(len(prices)):
            buy = prices[i]
            s = i + 1
            while s <= len(prices) - 1:
                print(s)
                print(f"buy: {buy}")
                profit = prices[s] - buy

                if profit > highest:
                    highest = profit
    
                s += 1
        return highest
        