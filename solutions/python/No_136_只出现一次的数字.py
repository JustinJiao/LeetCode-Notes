# LeetCode No.136 只出现一次的数字
# 题目链接: https://leetcode.cn/problems/single-number/description/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res