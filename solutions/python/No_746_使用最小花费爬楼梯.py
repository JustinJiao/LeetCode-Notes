# LeetCode No.746 使用最小花费爬楼梯
# 题目链接: https://leetcode.cn/problems/min-cost-climbing-stairs/description/

from typing import List

#方法一：动态规划
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) +1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2,len(cost) +1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[len(cost)]