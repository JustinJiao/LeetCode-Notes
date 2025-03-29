# LeetCode No.344 反转字符串
# 题目链接: https://leetcode.cn/problems/reverse-string/description/
from typing import List

#方法一：双指针
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left+=1
            right-=1
        

            
            
        
            
        