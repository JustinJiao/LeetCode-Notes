# LeetCode No.739 每日温度
# 题目链接:https://leetcode.cn/problems/daily-temperatures/description/
from typing import List

#方法一：单调栈
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        result = [0] *len(temperatures)
        for i in range(1,len(temperatures)):
            while len(stack) >0 and temperatures[i] > temperatures[stack[-1]]:
                result[stack[-1]] = i-stack[-1]
                stack.pop()
            stack.append(i)
        return result
