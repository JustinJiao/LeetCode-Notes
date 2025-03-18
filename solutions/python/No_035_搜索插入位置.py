# LeetCode No.35 搜索插入位置
# 题目链接: https://leetcode.cn/problems/search-insert-position/description/

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        middle = 0
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle -1
            elif nums[middle] < target:
                left = middle +1
            else:
                return middle
        return min(left, right) +1
        #right +1 其实可以这样写，因为无论哪种情况，right都是小的
        
        
        
            
        