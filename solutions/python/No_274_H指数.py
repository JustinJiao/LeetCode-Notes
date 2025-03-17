# LeetCode No.274 H指数
# 题目链接: https://leetcode.cn/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List

#方法一：暴力破解 用双层循环
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        maxH = len(citations)
        if maxH == 0:
            return 0
        while maxH > 0 :
            count = 0
            for val in citations:
                if(val >= maxH):
                    count+=1
            if count >= maxH:
                return maxH
            else:
                maxH -= 1
        return 0
        
#方法二：排序列表   
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        s = sorted(citations,reverse = True)
        h ,i = 0,0
        while i < len(citations) and s[i] > h:
            h+=1
            i+=1
        return h
    
#方法三：
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        counter = [0] * (n+1)
        total = 0
        for val in citations:
            if val >= n:
                counter[n]+=1
            else:
                counter[val]+= 1
        for i in range(n,-1,-1):
            total += counter[i]
            if total >= i:
                return i
        return 0
            
            
        
            
        