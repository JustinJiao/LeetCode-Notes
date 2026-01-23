# LeetCode No.674 最长连续递增序列
# 题目链接: https://leetcode.cn/problems/longest-continuous-increasing-subsequence/description/
from typing import List
# 方法一：动态规划
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result = 1
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] +1
            result = max(result,dp[i])
        return result
# 方法二：双指针，滑动窗口
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result = 1
        left = 0
        for right in range(1,len(nums)):
            if nums[right] <= nums[right-1]:
                result = max(result,right-left)
                left = right
        result = max(result, len(nums) - left)
        return result