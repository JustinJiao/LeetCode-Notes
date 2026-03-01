# LeetCode No.503 下一个更大元素二
# 题目链接: https://leetcode.cn/problems/next-greater-element-ii/description/

#方法一：单调栈
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        result = [-1] * n
        for i in range(2*n):
            while stack and nums[i%n] > nums[stack[-1]]:
                result[stack[-1]] = nums[i%n]
                stack.pop()
            if i < n:
                stack.append(i)
        return result