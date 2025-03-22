# LeetCode No.76 最小覆盖子串
# 题目链接: https://leetcode.cn/problems/minimum-window-substring/description/

#方法一：双指针（滑动窗口） + 哈希表
from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(dic)->bool:
            for key, val in need.items():
                if dic[key] < need[key]:
                    return False
            return True


        left = 0
        result = ""
        resultL = float('inf')
        subString = 0
        n = len(s)
        target = list[t]
        cnt = Counter()
        need = Counter(t)
        for right in range(n):
            cnt[s[right]] += 1
            while check(cnt):
                subString = right - left +1
                if subString < resultL:
                    result = s[left:right +1]
                    resultL = subString
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    cnt.pop(s[left])
                left +=1
        return result

        
        
        
        
            
        