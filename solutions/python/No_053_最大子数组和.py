# LeetCode No.53 最大子数组和
# 题目链接: https://leetcode.cn/problems/maximum-subarray/description/

from typing import List


#方法一：贪心
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        result = float('-inf')
        for i in range(len(nums)):
            cur = cur + nums[i]
            result = max(result,cur)
            if cur < 0:
                cur = 0
        return result

            
        