# LeetCode No.122 买卖股票的最佳时机二
# 题目链接: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1,len(prices)):
            cur = prices[i] - prices[i-1]
            if cur >0:
                result += cur
        return result
            
        