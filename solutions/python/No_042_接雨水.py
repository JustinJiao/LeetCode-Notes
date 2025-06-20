# LeetCode No.42 接雨水
# 题目链接: https://leetcode.cn/problems/trapping-rain-water/description/
from typing import List

#方法一：单调栈
class Solution:
    def trap(self, height: List[int]) -> int:
        sum = 0
        stack = [0]
        for i in range(1,len(height)):
            if height[i] <= height[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) >0 and height[i] > height[stack[-1]]:
                    middle = stack[-1]
                    stack.pop()
                    if len(stack)> 0:
                        h = min(height[i],height[stack[-1]])-height[middle]
                        w = i-stack[-1]-1
                        sum += h*w
                stack.append(i)
        return sum
            
        