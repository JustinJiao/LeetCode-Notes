# LeetCode No.738 单调递增的数字
# 题目链接: https://leetcode.cn/problems/monotone-increasing-digits/description/
from typing import List

#方法一：贪心
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        st = list(str(n))
        flag = len(st)
        for i in range(len(st)-1,0,-1):
            if st[i]<st[i-1]:
                st[i-1] = str(int(st[i - 1]) - 1)
                flag = i
        for i in range(flag,len(st)):
            st[i] = '9'
        return int("".join(st))