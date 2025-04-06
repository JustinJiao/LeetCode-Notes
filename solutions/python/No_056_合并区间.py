# LeetCode No.56 合并区间
# 题目链接: https://leetcode.cn/problems/merge-intervals/description/

from typing import List

#方法一：贪心
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: (x[0]))
        result = []
        for i in range(1,len(intervals)):
            if intervals[i][0] <=intervals[i-1][1]:
                intervals[i][0] = min(intervals[i-1][0],intervals[i][0])
                intervals[i][1] = max(intervals[i-1][1],intervals[i][1])
            else:
                result.append(intervals[i-1])
        result.append(intervals[-1])
        return result
        