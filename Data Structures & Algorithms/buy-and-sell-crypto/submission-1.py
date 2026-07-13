class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        mini=prices[0]
        for price in prices:
            mini=min(price,mini)
            curr=price-mini
            profit=max(curr,profit)
        return profit           
            
        