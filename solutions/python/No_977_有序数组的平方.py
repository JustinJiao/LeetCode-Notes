# LeetCode No.977 有序数组的平方
# 题目链接: https://leetcode.cn/problems/squares-of-a-sorted-array/description/


from typing import List

#方法一：暴力破解
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums

#方法二：双指针（前后指针）
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        result = [0]*len(nums)
        n = len(nums)-1
        while left <= right:
            if nums[left] ** 2 >= nums[right] ** 2:
                result[n] = nums[left] ** 2
                left +=1
            else:
                result[n] = nums[right] ** 2
                right -=1
            n -=1
        return result
            
        