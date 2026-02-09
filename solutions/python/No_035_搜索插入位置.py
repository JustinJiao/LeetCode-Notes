# LeetCode No.35 搜索插入位置
# 题目链接: https://leetcode.cn/problems/search-insert-position/description/

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0,len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else:
                return mid
        return left

        
        
        
            
        