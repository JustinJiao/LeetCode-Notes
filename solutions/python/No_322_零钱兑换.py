# LeetCode No.322 零钱兑换
# 题目链接: https://leetcode.cn/problems/coin-change/

#方法一：动态规划
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount ==0:
            return 0
        dp = [float('inf')] * (amount +1)
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(coins[i],amount+1):
                if dp[j-coins[i]] != float('inf'):
                    dp[j] = min(dp[j-coins[i]]+1,dp[j])
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]

            
            
        
            
        