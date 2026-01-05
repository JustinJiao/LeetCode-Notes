# LeetCode No.039 组合总和二
# 题目链接: https://leetcode.cn/problems/combination-sum-ii/description/

from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        result = []
        candidates.sort()
        def help(index,cursum):
            if cursum == target:
                result.append(path[:])
                return
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if cursum + candidates[i] > target:
                    break
                path.append(candidates[i])
                cursum += candidates[i]
                help(i+1,cursum)
                path.pop()
                cursum -= candidates[i]
        help(0,0)
        return result