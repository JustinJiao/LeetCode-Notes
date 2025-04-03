# LeetCode No.150 逆波兰表达式求值
# 题目链接: https://leetcode.cn/problems/evaluate-reverse-polish-notation/

from typing import List
#方法一：栈
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def div(x,y):
            if x * y >0:
                return int(x/y)
            else:
                return -(abs(x)//abs(y))
        stack = []
        result = 0
        for item in tokens:
            if item == "+":
                result = stack[-2]+stack[-1]
                stack.pop()
                stack.pop()
                stack.append(result)
            elif item == "-":
                result = stack[-2]-stack[-1]
                stack.pop()
                stack.pop()
                stack.append(result)
            elif item == "*":
                result = stack[-2] *stack[-1]
                stack.pop()
                stack.pop()
                stack.append(result)
            elif item == "/":
                result = div(stack[-2],stack[-1])
                stack.pop()
                stack.pop()
                stack.append(result)
            else:
                stack.append(int(item))
        return stack[0]


    
            
            
        
            
        