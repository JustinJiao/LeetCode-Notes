# LeetCode No.005 最长回文子串
# 题目链接: https://leetcode.cn/problems/longest-palindromic-substring/description/

#方法一：中心扩展法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <=1:
            return s
        start,max_length = 0,1
        def expand(left,right):
            nonlocal start,max_length
            while left >= 0 and right < n and s[left] == s[right]:
                cur_length = right - left +1
                if cur_length > max_length:
                    start = left #记录当前最长的回文子串的起始点
                    max_length = cur_length
                left -=1
                right +=1
        for i in range(n):
            expand(i,i) #奇数扩展
            expand(i,i+1) #偶数扩展
        return s[start:start + max_length]
#方法二：动态规划
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #dp[i][j]代表在[i-j]范围内是否是回文子串
        #dp[i][j] = if s[i] == s[j]:dp[i][j] = dp[i+1][j-1] else dp[i][j] = False
        n= len(s)
        if n <=1:
            return s
        dp = [[False] * n for _ in range(n)]
        start,max_length = 0,1
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i==j:
                    dp[i][j] = True
                elif s[i] == s[j]:
                    if j - i <=2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    max_length = j-i +1
                    start = i
        return s[start:start + max_length]