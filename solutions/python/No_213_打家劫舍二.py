# LeetCode No.213 打家劫舍二
# 题目链接: https://leetcode.cn/problems/house-robber-ii/description/

from typing import List

#方法一：动态规划
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob2(n):
            if len(n) < 2:
                return n[0]
            dp = [0] * len(n)
            dp[0] = n[0]
            dp[1] = max(n[0],n[1])
            for i in range(2,len(n)):
                dp[i] = max(n[i] + dp[i-2],dp[i-1])
            return dp[-1]
        if len(nums) < 2:
            return nums[0]
        n1 = nums[:len(nums)-1]
        n2 = nums[1:]
        return max(rob2(n1),rob2(n2))
        
            
            
            
        
            
        