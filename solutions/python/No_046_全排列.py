# LeetCode No.046 全排列
# 题目链接: https://leetcode.cn/problems/permutations/description/

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        used = [False] * len(nums)
        def help():
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                help()
                path.pop()
                used[i] = False
        help()
        return result
        
            
        