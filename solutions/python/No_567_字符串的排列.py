# LeetCode No.567 字符串的排列
# 题目链接: https://leetcode.cn/problems/permutation-in-string/description/

#方法一：滑动窗口+ 数组
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = [0] * 26
        for i in s1:
            target[ord(i)-ord('a')]+=1
        window = [0] * 26
        left = 0
        for right in range(len(s2)):
            cur = s2[right]
            window[ord(cur)-ord('a')] +=1
            if right - left +1 > len(s1):
                window[ord(s2[left])-ord('a')] -=1
                left +=1
            if window == target:
                return True
        return False
