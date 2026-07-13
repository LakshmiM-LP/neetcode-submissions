class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        profit=0
        for i in range(len(prices)):
            mini=min(mini,prices[i])

            curr=prices[i]-mini
            profit=max(profit,curr)
        return profit
