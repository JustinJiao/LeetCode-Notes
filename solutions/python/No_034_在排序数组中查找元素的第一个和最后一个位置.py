# LeetCode No.34 在排序数组中查找元素的第一个和最后一个位置
# 题目链接: https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/


from typing import List

#方法一：二分法
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def getRight(nums: List[int], target: int) -> List[int]:
            left, right = 0, len(nums)-1
            RB = -1
            while left <= right:
                middle = (left + right) //2
                if nums[middle] > target:
                    right = middle -1
                elif nums[middle] < target:
                    left = middle +1
                else:
                    RB = middle
                    left = middle +1
            return RB
        def getLeft(nums: List[int], target: int) -> List[int]:
            left, right = 0, len(nums)-1
            LB = -1
            while left <= right:
                middle = (left + right) //2
                if nums[middle] < target:
                    left = middle +1
                elif nums[middle] > target:
                    right = middle -1
                else:
                    LB = middle
                    right = middle -1
            return LB
        return [getLeft(nums,target),getRight(nums,target)]
        
            
        