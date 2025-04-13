# LeetCode No.416 分割等和子集
# 题目链接: https://leetcode.cn/problems/partition-equal-subset-sum/description/

from typing import List

#方法一：动态规划一维数组
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 != 0:
            return False
        target = sum_ // 2 
        dp = [0] * (target+1)
        for i in range(len(nums)):
            for j in range(target,nums[i]-1,-1):
                dp[j] = max(dp[j],nums[i] + dp[j-nums[i]])
                if dp[target] == target:
                    return True
        return False
        

        
        
            
        