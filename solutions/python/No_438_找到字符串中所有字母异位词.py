# LeetCode No.438 找到字符串中所有字母异位词
# 题目链接: https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/

from typing import List

#方法一：用Counter实现
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        target= Counter(p)
        left = 0
        result = []
        while left < len(s):
            right = left+len(p)
            temp = Counter(s[left:right])
            if temp == target:
                result.append(left)
            left+=1
        return result   
        
        
#方法二：defaultdict   
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        p_l = [0]*26
        s_l = [0]*26
        result = []
        if len(s)< len(p):
            return result
        for i in range(len(p)):
            p_l[ord(p[i])-ord('a')] +=1
            s_l[ord(s[i])-ord('a')] +=1
        if p_l == s_l:
            result.append(0)
        left = 0
        while left < len(s)-len(p):
            s_l[ord(s[left])-ord('a')] -=1
            s_l[ord(s[left+len(p)])-ord('a')] +=1
            if s_l == p_l:
                result.append(left+1)
            left+=1
        return result
    

            
            
        
            
        