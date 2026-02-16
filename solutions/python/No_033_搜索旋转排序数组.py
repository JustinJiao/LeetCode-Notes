# LeetCode No.33 搜索旋转排序数组
# 题目链接: https://leetcode.cn/problems/search-in-rotated-sorted-array/description/

# 方法一：二分查找
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0,len(nums)-1
        while left <= right:
            mid = (left + right) //2
            if nums[mid] == target:
                return mid
            elif nums[left]<= nums[mid]:#左边有序
                if nums[left] <= target <nums[mid]:
                    right = mid-1
                else:
                    left = mid +1
            else: #右边有序
                if nums[mid] < target <=nums[right]:
                    left = mid +1
                else:
                    right = mid -1
        return -1
