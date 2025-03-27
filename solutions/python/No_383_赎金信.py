# LeetCode No.242 有效的字母异位词
# 题目链接: https://leetcode.cn/problems/valid-anagram/description/

from typing import List

#方法一：数组
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashTable = [0]*26
        for i in range(len(magazine)):
            hashTable[ord(magazine[i])-ord('a')] +=1
        for i in range(len(ransomNote)):
            hashTable[ord(ransomNote[i])-ord('a')]-=1
        for i in hashTable:
            if i <0:
                return False
        return True        
        
        
#方法二：defaultdict   
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import defaultdict
        m = defaultdict(int)
        for i in magazine:
            m[i] +=1
        for i in ransomNote:
            n = m.get(i)
            if not n:
                return False
            else:
                m[i] -= 1
        return True
    
#方法三：Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        cnt = Counter(magazine)
        for i in ransomNote:
            if i in cnt:
                cnt[i] -= 1
                if cnt[i] == 0:
                    del cnt[i]
            else:
                return False
        return True
            
            
        
            
        