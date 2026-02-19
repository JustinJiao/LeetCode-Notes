# LeetCode No.64 最小路径和
# 题目链接: https://leetcode.cn/problems/minimum-path-sum/description/
#方法一：动态规划
class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        
        # 初始化第一行
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = dp[j-1] + grid[0][j]
        
        # 更新后续行
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        
        return dp[-1]
