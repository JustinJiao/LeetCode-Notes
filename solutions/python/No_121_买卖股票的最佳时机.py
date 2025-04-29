# LeetCode No.121 买卖股票的最佳时机
# 题目链接: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/

#方法一：动态规划
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1],-prices[i])
        return max(dp[-1][0],dp[-1][1])

#方法二：优化动态规划
#直接使用两个数字进行追踪即可
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp0 = 0
        dp1 = -prices[0]
        for i in range(1,len(prices)):
            dp0 = max(dp0,dp1+prices[i])
            dp1 = max(dp1,-prices[i])
        return max(dp0,dp1)
        