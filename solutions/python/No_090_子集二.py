# LeetCode No 90 子集二
# 题目链接: https://leetcode.cn/problems/subsets-with-dup/

#回溯模板
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        nums.sort()
        def help(startIndex):
            result.append(path[:])
            for i in range(startIndex,len(nums)):
                if i> startIndex and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                help(i+1)
                path.pop()
        help(0)
        return result


