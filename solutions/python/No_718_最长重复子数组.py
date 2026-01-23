# LeetCode No.718 最长重复子数组
# 题目链接: https://leetcode.cn/problems/maximum-length-of-repeated-subarray/description/
from typing import List
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        #dp[i][j]以i-1结尾的nums1，和以j-1结尾的nums2，的最长重复子数组
        #递推公式：if nums1[i-1] == nums2[j-1]: dp[i][j] = dp[i-1][j-1] +1
        result = 0
        dp = [[0] * (len(nums2)+1) for _ in range(len(nums1)+1)]
        for i in range(1,len(nums1)+1):
            for j in range(1,len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] +1
                result = max(result,dp[i][j])
        return result