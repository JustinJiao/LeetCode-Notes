# LeetCode No.392 判断子序列
# 题目链接: https://leetcode.cn/problems/is-subsequence/description/

from typing import List,Optional

#方法一：动态规划
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[len(s)][len(t)] == len(s)
#方法二：双指针
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        if not s:
            return True
        for right in range(len(t)):
            if s[left] == t[right]:
                left +=1
            if left == len(s):
                return True
        return False
            
        
            
        