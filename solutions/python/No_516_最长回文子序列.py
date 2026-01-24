# LeetCode No.516 最长回文子序列
# 题目链接: https://leetcode.cn/problems/longest-palindromic-subsequence/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] +2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[0][len(s)-1]