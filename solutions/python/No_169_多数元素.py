# LeetCode No.169 多数元素
# 题目链接: https://leetcode.cn/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numHash = {}
        result = 0
        for val in nums:   #O(N)
            if val not in numHash:
                numHash[val] =1
            numHash[val] +=1
        return max(numHash,key=numHash.get)
        
            
        