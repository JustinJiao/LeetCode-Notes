# LeetCode No.28 找出字符串中第一个匹配的下标
# 题目链接: https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

from typing import List

#方法一：暴力破解
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == len(needle):
            if haystack == needle:
                return 0
            else:
                return -1
        if len(haystack) < len(needle):
            return -1
        for left in range(len(haystack)):
            right = left + len(needle)
            cur = haystack[left:right]
            if cur == needle:
                return left
        return -1

#方法二：KMP
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def getnext(s):
            next_ = [0]*len(s)
            j = 0
            for i in range(1,len(s)):
                while j > 0 and s[i] != s[j]:
                    j = next_[j-1]
                if s[i] == s[j]:
                    j+=1
                next_[i] = j
            return next_
        j = 0
        next_ = getnext(needle)
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next_[j-1]
            if haystack[i] == needle[j]:
                j+=1
            if j == len(needle):
                return i-len(needle) +1
        return -1

        
        
        
            
        