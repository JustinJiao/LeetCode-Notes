# LeetCode No.42 接雨水
# 题目链接: https://leetcode.cn/problems/trapping-rain-water/description/
from typing import List

#方法一：单调栈
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        result = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                mid = height[stack[-1]]
                stack.pop()
                if stack:
                    left= stack[-1]
                    right= i
                    h = min(height[left],height[right])-mid
                    width = right-left -1
                    result += h * width
            stack.append(i)
        return result

            
        