# LeetCode No.001 两数之和
# 题目链接: https://leetcode.cn/problems/two-sum/description/

from typing import List

#方法一：用字典存储
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_num = {}
        for i, v in enumerate(nums):
            secNum = target - v
            if secNum in index_num:
                return [index_num[secNum],i]
            index_num[v] = i
        
            
        