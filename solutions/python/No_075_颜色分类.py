# LeetCode No.75 颜色分类
# 题目链接: https://leetcode.cn/problems/sort-colors/description/


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left,i,right = 0,0,len(nums)-1
        while i <= right:
            if nums[i] == 0:
                nums[left],nums[i] = nums[i],nums[left]
                left +=1
                i +=1
            elif nums[i] == 1:
                i+=1
            else:
                nums[i],nums[right] = nums[right],nums[i]
                right-=1
        