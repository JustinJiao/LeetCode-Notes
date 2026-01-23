# LeetCode No.300 最长递增子序列
# 题目链接: https://leetcode.cn/problems/longest-increasing-subsequence/description/
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        resulst = 1
        dp = [1] * len(nums)
        dp[0] = 1
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
            resulst = max(resulst,dp[i])
        return resulst
