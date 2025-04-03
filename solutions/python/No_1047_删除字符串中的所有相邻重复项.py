# LeetCode No.977 有序数组的平方
# 题目链接: https://leetcode.cn/problems/squares-of-a-sorted-array/description/


from typing import List

#方法一：栈
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for item in s:
            if stack:
                temp = stack[-1]
                if temp == item:
                    stack.pop()
                    continue
                else:
                    stack.append(item)
            else:
                stack.append(item)
        return "".join(stack)

            
        