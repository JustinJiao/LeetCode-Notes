# LeetCode No.455 分发饼干
# 题目链接: https://leetcode.cn/problems/assign-cookies/description/

from typing import List

#方法一：使用贪心策略分大饼干
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        index = len(s)-1
        cnt =0
        for i in range(len(g)-1,-1,-1):
            if index >= 0 and s[index] >= g[i]:
                cnt +=1
                index-=1
        return cnt
    
#方法二：用贪心策略分小饼干
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cnt = 0
        left, right = 0,0
        while left < len(g) and right < len(s):
            if s[right] >= g[left]:
                cnt +=1
                left +=1
                right +=1
            else:
                right +=1
        return cnt

        
        
            
        