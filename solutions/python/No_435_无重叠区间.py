# LeetCode No.435 无重叠区间
# 题目链接: https://leetcode.cn/problems/non-overlapping-intervals/description/

from typing import List

#方法一：排序+贪心
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key = lambda x:(x[0]))
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                res +=1
                intervals[i][1] = min(intervals[i][1],intervals[i-1][1])
        return res

        
        
            
        