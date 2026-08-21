class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #slinding window 101 problem
        profit = 0
        min_p = prices[0]
        max_p = prices[0]
        i,j = 0,1

        for indx,val in enumerate(prices):
            if indx == 0:
                continue
            
            if val <= min_p:
                min_p = val
                continue
            else:
                curr_profit = val - min_p
                if curr_profit > profit:
                    profit = curr_profit 

        return profit
                    