# LeetCode No.153 寻找旋转排序数组中的最小值
# 题目链接: https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/description/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0,len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid +1
            else:
                right = mid
        return nums[left]