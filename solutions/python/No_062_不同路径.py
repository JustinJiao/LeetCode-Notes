# LeetCode No.62 不同路径
# 题目链接: https://leetcode.cn/problems/unique-paths/description/

#方法一：动态规划
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] =1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] +dp[i][j-1]
        return dp[m-1][n-1]

#方法二：动态规划（空间优化）
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1,m):
            for j in range(1,n):
                dp[j] = dp[j] + dp[j-1]
        return dp[n-1]
        
        
        
            
        