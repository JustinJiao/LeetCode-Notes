# LeetCode No.714 买卖股票的最佳时机含手续费
# 题目链接: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp0 = -prices[0] #持有
        dp1 = 0 #未持有
        for i in range(1,len(prices)):
            t0 = max(dp0,dp1 - prices[i])
            t1 = max(dp1,dp0+prices[i]-fee)
            dp0,dp1 = t0,t1
        return dp1