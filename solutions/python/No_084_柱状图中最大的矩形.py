# LeetCode No.84 柱状图中最大的矩形
# 题目链接: https://leetcode.cn/problems/largest-rectangle-in-histogram/description/

from typing import List

#方法一：单调栈
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.insert(0,0)
        heights.append(0)
        stack = [0]
        result = 0
        for i in range(1,len(heights)):
            if heights[i] >= heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[i] < heights[stack[-1]]:
                    mid = heights[stack[-1]]
                    stack.pop()
                    if stack:
                        left = stack[-1]
                        right = i
                        w = right-left-1
                        result = max(result,w*mid)
                stack.append(i)
        return result
        
        