# LeetCode No.491 非递减子序列
# 题目链接:https://leetcode.cn/problems/non-decreasing-subsequences/description/

from typing import List

#方法一：动态规划二维数组
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        path = []
        result =[]
        def help(startIndex):
            if len(path) >=2:
                result.append(path[:])
            used = set()
            for i in range(startIndex,len(nums)):
                if nums[i] in used:
                    continue
                if len(path) == 0 or nums[i] >= path[-1]:
                    used.add(nums[i])
                    path.append(nums[i])
                    help(i+1)
                    path.pop()
        help(0)
        return result
            
        