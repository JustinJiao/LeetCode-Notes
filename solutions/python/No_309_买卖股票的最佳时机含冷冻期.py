# LeetCode No.309 买卖股票的最佳时机含冷冻期
# 题目链接: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #首先，这个包含冷冻期，之前是分为持股和不持股两个状态，因为包含冷冻期，那么就分为四个状态
        #1. 持股状态，不变 dp1
        #2. 卖出后不持股状态 dp2
        #3. 卖出 dp3
        #4. 冷冻期 dp4
        #也就是加入了一个冷冻期，然后把不持股状态分为卖出当天，和非卖出当天
        #dp1: 持股状态：可以由这么几个导出：（1）dp1 --前一天就持股, 
                                     #（2）dp2 - prices[i] -- 卖出过不持股状态后买入
                                     #（3）dp4 - prices[i] -- 前一天是冷冻期
        #dp2:卖出后不持股状态：（1）dp2 -- 前一天就是这个状态
        #                   （2）dp4 前一天是冷冻期
        #dp3:卖出股票当天      （1）dp1 + prices[i] -- 前一天是持股的情况
        #dp4 :冷冻期。        （1）dp3 -- 前一天是卖出的情况

        dp1 = -prices[0]
        dp2 = 0
        dp3 = 0
        dp4 = 0
        for i in range(1,len(prices)):
            t1 = max(dp1,dp2-prices[i],dp4-prices[i])
            t2 = max(dp2,dp4)
            t3 = dp1+prices[i]
            t4 = dp3
            dp1,dp2,dp3,dp4= t1,t2,t3,t4
        return max(dp2,dp3,dp4)