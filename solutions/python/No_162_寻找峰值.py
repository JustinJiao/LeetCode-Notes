# LeetCode No.162 寻找峰值
# 题目链接: https://leetcode.cn/problems/find-peak-element/

#方法一：二分查找
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left,right = 0,len(nums)-1
        while left < right:
            mid = (left + right) //2
            if nums[mid] <nums[mid+1]:
                left = mid +1
            else:
                right = mid
        return left