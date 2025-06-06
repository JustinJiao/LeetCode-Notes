# LeetCode No.474 一和零
# 题目链接:https://leetcode.cn/problems/ones-and-zeroes/description/

from typing import List

#方法一：动态规划二维数组
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        for st in strs:
            zero = st.count('0')
            one = len(st) - zero
            for i in range(m,zero-1,-1):
                for j in range(n,one-1,-1):
                    dp[i][j] = max(dp[i][j],dp[i-zero][j-one]+1)
        return dp[m][n]
            
        