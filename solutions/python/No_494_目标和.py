# LeetCode No.494 目标和
# 题目链接:https://leetcode.cn/problems/target-sum/description/

from typing import List

#方法一：动态规划二维数组
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (target + sum(nums)) % 2 == 1:
            return 0
        if abs(target) > sum(nums):
            return 0

        bagV = (target + sum(nums))//2
        dp = [[0] * (bagV +1) for _ in range(len(nums))]
        dp[0][0] =1

        if nums[0] <= bagV:
            dp[0][nums[0]] =1

        numZero = 0
        for i in range(len(nums)):
            if nums[i]  == 0:
                numZero +=1
            dp[i][0] = int(math.pow(2,numZero))
        
        for i in range(1,len(nums)):
            for j in range(1,bagV+1):
                if nums[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]

        return dp[len(nums)-1][bagV]
    
#方法一：动态规划一维数组
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (sum(nums) + target) %2 ==1:
            return 0
        if abs(target) > sum(nums):
            return 0
        
        bagV = (sum(nums) + target) //2
        
        dp = [0] * (bagV+1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(bagV,nums[i]-1,-1):
                dp[j] += dp[j-nums[i]]
        return dp[bagV]
        

        
        
            
        