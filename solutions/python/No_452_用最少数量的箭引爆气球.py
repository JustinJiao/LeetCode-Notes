# LeetCode No.452 用最少数量的箭引爆气球
# 题目链接: https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/description/

from typing import List

#方法一：排序+贪心
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        result = 1
        points.sort(key = lambda x : (x[0]))
        for i in range(1,len(points)):
            if points[i][0] > points[i-1][1]:
                result +=1
            else:
                points[i][1] = min(points[i-1][1],points[i][1])
        return result

        
        
            
        