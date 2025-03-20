# LeetCode No.844 比较含退格的字符串
# 题目链接: https://leetcode.cn/problems/backspace-string-compare/description/

from typing import List

#方法一：快慢指针
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def r (s:str) -> str:
            ss = list(s)
            left = 0
            for right in range(len(ss)):
                if ss[right] != "#":
                    ss[left] = ss[right]
                    left +=1
                elif left >0:
                    left -=1
            ss = ss[:left]
            return "".join(ss)
        return r(s) == r(t)
        
            
        