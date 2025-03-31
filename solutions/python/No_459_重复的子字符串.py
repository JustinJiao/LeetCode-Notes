# LeetCode No.459 重复的子字符串
# 题目链接: https://leetcode.cn/problems/repeated-substring-pattern/description/

from typing import List

#方法一：KMP算法
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def getnext(s:str):
            next_ = [0]*len(s)
            j = 0
            for i in range(1,len(s)):
                while j > 0 and s[j] != s[i]:
                    j = next_[j-1]
                if s[j] == s[i]:
                    j +=1
                next_[i] = j
            return next_
        next_ = getnext(s)
        if len(s) % (len(s)-next_[-1]) == 0 and next_[-1] != 0:
            return True
        return False

#方法二：暴力破解
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        subs = [s[0]]
        for i in range(1,len(s)):
            if len(s) % i != 0:
                continue
            subs.append(s[:i])
        for i in subs:
            times = len(s) // len(i)
            if times == 1:
                continue
            cur = "".join(i*times)
            if cur == s:
                return True
        return False
        
        
        
            
        