# LeetCode No.367 有效的完全平方数
# 题目链接: https://leetcode.cn/problems/valid-perfect-square/description/
from typing import List

#方法一：二分法
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left , right = 0, num
        while left <= right:
            mid = (left + right ) //2
            if mid*mid > num:
                right = mid -1
            elif mid * mid < num:
                left = mid +1
            else:
                return True
        return False

            
            
        
            
        