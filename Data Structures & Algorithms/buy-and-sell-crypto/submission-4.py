class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpf = 0
        minbp = prices[0]
        for indx,val in enumerate(prices):
            # print(val,indx)
            print(minbp,maxpf)
            if maxpf < val - minbp:
                maxpf = val - minbp
            
            if val < minbp:
                minbp = val
            
        if maxpf > 0:
            return maxpf
        else:
            return 0