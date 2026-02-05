# LeetCode No.541 翻转字符串二
# 题目链接: https://leetcode.cn/problems/reverse-string-ii/description/

from typing import List

#方法一：暴力解法
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        st = list(s)
        left = 0
        end = len(st) -1
        for right in range(len(st)):
            if right - left +1  == 2*k:
                mid = left +k-1
                while left < mid:
                    st[left],st[mid] = st[mid],st[left]
                    left +=1
                    mid -=1
                left = right+1
            elif end - left+1 < 2 * k and end-left+1 >= k:
                mid = left +k-1
                while left < mid:
                    st[left],st[mid] = st[mid],st[left]
                    left +=1
                    mid -=1
                break
            elif end - left+1 < k:
                while left < end:
                    st[left],st[end] = st[end],st[left]
                    left +=1
                    end -=1
        return "".join(x for x in st)
#方法二：构造函数
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(l):
            left, right = 0, len(l)-1
            while left < right:
                l[left],l[right] = l[right], l[left]
                left +=1
                right -=1
            return l

        st = list(s)
        for cur in range(0,len(st),2*k):
            st[cur:cur+k] = reverse(st[cur:cur+k])
        return "".join(st)
        
        
            
        