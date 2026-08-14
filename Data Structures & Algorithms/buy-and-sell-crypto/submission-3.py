class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        diff = 0
        for i in range(1,len(prices)):
            
            temp_diff = prices[i] - min_price
            if temp_diff > diff:
                diff = temp_diff
            
            if min_price > prices[i]:
                min_price = prices[i]

        
        return diff
        
        