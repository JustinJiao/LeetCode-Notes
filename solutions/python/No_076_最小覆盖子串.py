# LeetCode No.76 最小覆盖子串
# 题目链接: https://leetcode.cn/problems/minimum-window-substring/description/

#方法一：双指针（滑动窗口） + 哈希表
from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(dic,target):
            return all(dic[k] >=target[k] for k in target)

        left = 0
        substring = ""
        sublength = float("inf")
        target = Counter(t)
        dic = Counter()
        for right in range(0,len(s)):
            dic[s[right]]+=1
            while check(dic,target):
                curlength = right-left +1
                if curlength<sublength:
                    substring = s[left:right+1]
                    sublength = len(substring)
                dic[s[left]]-=1
                if dic[s[left]] == 0:
                    dic.pop(s[left])
                left +=1
        return substring
        
#优化：使用need来追踪，当遍历一个s的时候，那么此时加入进去的字母看是否对于覆盖t有效，如果有效那么need-1
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = len(t)
        left = 0
        substring = ""
        sublength = float("inf")
        target = Counter(t)
        dic = Counter()
        for right in range(0,len(s)):
            dic[s[right]]+=1
            if dic[s[right]]<=target[s[right]]:
                need-=1
            while need == 0:
                curlength = right-left +1
                if curlength<sublength:
                    substring = s[left:right+1]
                    sublength = len(substring)
                dic[s[left]]-=1
                if dic[s[left]] < target[s[left]]:
                    need +=1
                left +=1
        return substring
        
        
            
        