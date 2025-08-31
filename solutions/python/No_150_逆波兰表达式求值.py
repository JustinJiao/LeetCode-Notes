# LeetCode No.150 逆波兰表达式求值
# 题目链接: https://leetcode.cn/problems/evaluate-reverse-polish-notation/

from typing import List
#方法一：栈
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l = []
        result = 0
        for i in tokens:
            if i == '+':
                n1 = int(l.pop())
                n2 = int(l.pop())
                result  = n2 + n1
                l.append(result)
            elif i == '-':
                n1 = int(l.pop())
                n2 = int(l.pop())
                result = (n2-n1)
                l.append(result)
            elif i == '*':
                n1 = int(l.pop())
                n2 = int(l.pop())
                result = (n2 * n1)
                l.append(result)
            elif i == '/':
                n1 = int(l.pop())
                n2 = int(l.pop())
                result = int(n2/n1)
                l.append(result)
            else:
                l.append(int(i))
        return l[0]

    
            
            
        
            
        