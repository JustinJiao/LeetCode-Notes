# LeetCode No.763 划分字母区间
# 题目链接: https://leetcode.cn/problems/partition-labels/description/

from typing import List

#方法一：字典+贪心
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        s1 = {}
        result = []
        left, right = 0,0
        for i, char in enumerate(s):
            s1[char] = i
        for i, char in enumerate(s):
            right = max(s1[char],right)
            if i == right:
                result.append(right -left +1)
                left = i +1
        return result