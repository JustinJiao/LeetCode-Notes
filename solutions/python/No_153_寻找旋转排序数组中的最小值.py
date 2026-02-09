# LeetCode No.151 反转字符串中的单词
# 题目链接: https://leetcode.cn/problems/reverse-words-in-a-string/description/
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