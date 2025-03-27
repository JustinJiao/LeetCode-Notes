# LeetCode No.242 有效的字母异位词
# 题目链接: https://leetcode.cn/problems/valid-anagram/description/

import bisect
from typing import List

#方法一：数组
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashTable = [0]*26
        for i in range(len(s)):
            hashTable[ord(s[i])-ord('a')] +=1
        for i in range(len(t)):
            hashTable[ord(t[i])-ord('a')] -= 1
        for i in range(26):
            if hashTable[i] != 0:
                return False
        return True
        
        
#方法二：defaultdict   
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        s1 = defaultdict(int)
        t1 = defaultdict(int)
        for i in s:
            s1[i]+=1
        for i in t:
            t1[i] +=1
        return s1 == t1
    
#方法三：Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        s1 = Counter(s)
        t1 = Counter(t)
        return s1 == t1
            
            
        
            
        