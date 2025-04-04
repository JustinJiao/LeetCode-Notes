# LeetCode No.376 摆动序列
# 题目链接:https://leetcode.cn/problems/wiggle-subsequence/
from typing import List
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        pre = 0
        cur = 0
        result = 1
        for i in range(len(nums)-1):
            cur = nums[i+1] - nums[i]
            if (pre >=0 and cur <0 ) or (pre<=0 and cur >0):
                result +=1
                pre = cur
        return result