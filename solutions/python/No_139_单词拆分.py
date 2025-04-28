# LeetCode No.139 单词拆分
# 题目链接:https://leetcode.cn/problems/word-break/description/

from typing import List

#方法一：动态规划一维数组
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) +1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(i):
                s1 = s[j:i]
                if s1 in wordDict and dp[j]:
                    dp[i] = True
        return dp[len(s)]

        
        
            
        