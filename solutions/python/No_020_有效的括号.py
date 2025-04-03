# LeetCode No.20 有效的括号
# 题目链接: https://leetcode.cn/problems/valid-parentheses/description/

#方法一：栈
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item =="(":
                stack.append(")")
            elif item == "[":
                stack.append("]")
            elif item == "{":
                stack.append("}")
            elif not stack or stack[-1] != item:
                return False
            else:
                stack.pop()
        if not stack:
            return True
        else:
            return False

            
            
        
            
        