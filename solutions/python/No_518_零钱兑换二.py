# LeetCode No.518 零钱兑换二
# 题目链接:https://leetcode.cn/problems/coin-change-ii/description/

from typing import List

#方法一：动态规划二维数组
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0]*(amount+1) for _ in range(len(coins))]
        for j in range(1,amount+1):
            if j % coins[0] == 0:
                dp[0][j] = 1
        for i in range(len(coins)):
            dp[i][0] = 1
        for i in range (1,len(coins)):
            for j in range(1,amount+1):
                if j<coins[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-coins[i]]+dp[i-1][j]
        return dp[len(coins)-1][amount]
#方法一：动态规划一维数组
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount +1)
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(coins[i],amount +1):
                dp[j] = dp[j] + dp[j-coins[i]]
        return dp[amount]

        
        
            
        