# LeetCode No.343 整数拆分
# 题目链接: https://leetcode.cn/problems/integer-break/description/

from typing import List

#方法一：动态规划
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[2] =1
        for i in range(3,n+1):
            for j in range(1,i):
                dp[i] = max(j*(i-j),j*dp[i-j],dp[i])
        return dp[n]
        

            
            
        
            
        