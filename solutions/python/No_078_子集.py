# LeetCode No 78 子集
# 题目链接: https://leetcode.cn/problems/subsets/

#回溯模板
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        def help(startIndex):
            result.append(path[:])
            if startIndex >= len(nums):
                return
            for i in range(startIndex,len(nums)):
                path.append(nums[i])
                help(i+1)
                path.pop()
        help(0)
        return result


