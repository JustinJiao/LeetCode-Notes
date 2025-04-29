# LeetCode No.122 买卖股票的最佳时机二
# 题目链接: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description/

from typing import List

#方法一：贪心策略
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1,len(prices)):
            cur = prices[i] - prices[i-1]
            if cur >0:
                result += cur
        return result
            
#方法二：动态规划
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp0 = 0
        dp1 = -prices[0]
        for i in range(1,len(prices)):
            dp0 = max(dp0,dp1+prices[i])
            dp1 = max(dp1,dp0-prices[i])
        return max(dp1,dp0)