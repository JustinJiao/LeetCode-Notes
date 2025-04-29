# LeetCode No.188 买卖股票的最佳时机四
# 题目链接: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/description/

#方法二：优化动态规划
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [0]* ((2*k)+1)
        for i in range(1,len(dp)):
            if i %2 ==0:
                dp[i] = 0
            else:
                dp[i] = -prices[0]
        for i in range(1,len(prices)):
            for j in range(1,len(dp)):
                if j %2 == 0:
                    dp[j] = max(dp[j],dp[j-1]+prices[i])
                else:
                    dp[j] = max(dp[j],dp[j-1]-prices[i])
        return dp[2*k]