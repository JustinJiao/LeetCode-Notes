# LeetCode No.041 缺失的第一个正数
# 题目链接: https://leetcode.cn/problems/first-missing-positive/description/

#方法一：安排下标
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1<=nums[i]<=n and nums[i] != nums[nums[i]-1]:
                correct_index = nums[i]-1
                nums[i],nums[correct_index] = nums[correct_index],nums[i]
        for i in range(n):
            if nums[i]!= i+1:
                return i+1
        return n+1

#方法二：哈希表
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)
        for i in range(1,len(nums)+1):
            if i not in num_set:
                return i
        return len(nums)+1