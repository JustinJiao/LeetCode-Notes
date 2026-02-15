# LeetCode No.003 无重复字符的最长子串
# 题目链接: https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/

from typing import List

#方法一：滑动窗口+ dic（计数）
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        left = 0
        start = 0
        result = 0
        dic = defaultdict(int)
        for right in range(len(s)):
            cur = s[right]
            dic[cur] +=1
            while dic[cur] >1:
                dic[s[left]] -=1
                left +=1
            if right - left +1 > result:
                result = right-left +1
        return result
        
#方法二：滑动窗口+ dic（存储索引）
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        left = 0
        result = 0
        for right,ch in enumerate(s):
            if ch in last_index and last_index[ch] >= left:
                left = last_index[ch]+1
            last_index[ch] = right
            result = max(result,right-left+1)
        return result
        