# LeetCode No.704 二分查找
# 题目链接: https://leetcode.cn/problems/binary-search/description/

from typing import List

#方法一：二分查找法
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle-1
            elif nums[middle] < target:
                left = middle +1
            else:
                return middle
        return -1
            
        
            
        