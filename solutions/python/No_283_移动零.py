# LeetCode No.283 移动零
# 题目链接: https://leetcode.cn/problems/move-zeroes/description/

from typing import List

#方法一：快慢指针
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left],nums[right] = nums[right],nums[left]
                left +=1
            right +=1

            
            
        
            
        