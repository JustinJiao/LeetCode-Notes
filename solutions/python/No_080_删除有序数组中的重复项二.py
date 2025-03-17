# LeetCode No.80 删除有序数组中的重复项二
# 题目链接: https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

from typing import List

#方法一：双指针
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return len(nums)
        left, right = 2,2
        while right < len(nums):      #O(N)
            if nums[right] != nums[left-2]:
                nums[left] = nums[right]
                left += 1
            right +=1
        return left
        