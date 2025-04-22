# LeetCode No.377 组合总和四
# 题目链接:https://leetcode.cn/problems/combination-sum-iv/description/

from typing import List

#方法一：动态规划二维数组
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [[0] * (target +1) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = 1
            
        for j in range(1,target+1):
            for i in range(len(nums)):
                if j >= nums[i]:
                    dp[i][j] = dp[-1][j-nums[i]]+dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
#方法一：动态规划一维数组
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for j in range(target+1):
            for i in range(len(nums)):
                if j >= nums[i]:
                    dp[j] = dp[j] + dp[j-nums[i]]
        return dp[target]
        

        
        
            
        