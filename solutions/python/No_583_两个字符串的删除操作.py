# LeetCode No.583 两个字符串的删除操作
# 题目链接: https://leetcode.cn/problems/delete-operation-for-two-strings/description/

#方法一：动态规划 求最长公共子序列
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        result = 0
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            result = max(result,dp[i][j])
        return len(word1)-result + len(word2)-result
#方法二：优化动态规划 直接求删除次数
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        result = 0
        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j
        dp[0][0] = 0 
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+2)
        return dp[len(word1)][len(word2)]