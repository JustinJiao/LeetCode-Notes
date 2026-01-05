# LeetCode No.039 组合总和
# 题目链接: https://leetcode.cn/problems/combination-sum/description/
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        result = []
        def help(startIndex,cursum):
            if cursum > target:
                return
            if cursum == target:
                result.append(path[:])
                return
            for i in range(startIndex,len(candidates)):
                path.append(candidates[i])
                cursum += candidates[i]
                help(i,cursum)
                cursum -= candidates[i]
                path.pop()
        help(0,0)
        return result
