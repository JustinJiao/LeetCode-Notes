# LeetCode No.279 完全平方
# 题目链接: https://leetcode.cn/problems/perfect-squares/description/

#方法一：动态规划
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1,int(n**0.5)+1):
            num = i * i
            for j in range(num,n+1):
                dp[j] = min(dp[j],dp[j-num]+1)
        return dp[n]

            
            
        
            
        