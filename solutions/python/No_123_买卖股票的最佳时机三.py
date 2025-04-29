# LeetCode No.123 买卖股票的最佳时机三
# 题目链接: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/description/

#方法一：动态规划
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 5 for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        dp[0][3] = -prices[0]
        dp[0][4] = 0
        for i in range(1,len(prices)):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
            dp[i][2] = max(dp[i-1][2],dp[i-1][1]+prices[i])
            dp[i][3] = max(dp[i-1][3],dp[i-1][2]-prices[i])
            dp[i][4] = max(dp[i-1][4],dp[i-1][3]+prices[i])
        return dp[-1][4]

#方法二：优化动态规划
#直接使用四个数字进行追踪即可
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp0 = 0
        dp1 = -prices[0]
        dp2 = 0
        dp3 = -prices[0]
        dp4 = 0
        for i in range(1,len(prices)):
            dp1 = max(dp1,dp0-prices[i])
            dp2 = max(dp2,dp1+prices[i])
            dp3 = max(dp3,dp2-prices[i])
            dp4 = max(dp4,dp3+prices[i])
        return dp4
        