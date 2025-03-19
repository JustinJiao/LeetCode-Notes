# LeetCode No.69 x的平方根
# 题目链接: https://leetcode.cn/problems/sqrtx/description/

from typing import List


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right , result = 0,x,-1
        while left <= right:
            middle = (left + right ) //2
            if middle * middle > x:
                right = middle -1
            else:
                result = middle
                left = middle +1
        return result
        
        
        
        
            
        