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
        
        
#方法二：滑动窗口+ dic（计数）
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        left = 0
        target = [0] * 26
        for char in p:
            target[ord(char)-ord('a')] +=1
        window = [0]*26
        for right in range(len(s)):
            window[ord(s[right])-ord('a')]+=1
            curlength = right - left +1
            if curlength > len(p):
                window[ord(s[left])-ord('a')]-=1
                left +=1
            if window == target:
                result.append(left)
        return result
    

            
            
        
            
        