# LeetCode No.509 斐波那契数
# 题目链接: https://leetcode.cn/problems/fibonacci-number/description/

from typing import List

#方法一：动态规划
class Solution:
    def fib(self, n: int) -> int:
        f = [0] *31
        f[0] = 0
        f[1] = 1
        for i in range(2,n+1):
            f[i] = f[i-1] +f[i-2]
        return f[n]

        
        
        
            
        