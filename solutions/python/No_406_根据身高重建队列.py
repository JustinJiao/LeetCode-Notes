# LeetCode No.406 根据身高重建队列
# 题目链接: https://leetcode.cn/problems/queue-reconstruction-by-height/description/

from typing import List

#方法一：贪心
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x:(-x[0],x[1]))
        result = []
        for i in people:
            result.insert(i[1],i)
        return result

            
            
        
            
        