# LeetCode No.198 打家劫舍
# 题目链接: https://leetcode.cn/problems/house-robber/description/

from typing import List

#方法一：动态规划
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <2:
            return nums[0]
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        return dp[-1]
            
            
            
            
        
            
        