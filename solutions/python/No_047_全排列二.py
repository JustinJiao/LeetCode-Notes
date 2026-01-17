# LeetCode No.047 全排列二
# 题目链接: https://leetcode.cn/problems/permutations-ii/description/
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        used = [False] * len(nums)
        nums.sort()
        def help():
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                    continue
                used[i] = True
                path.append(nums[i])
                help()
                path.pop()
                used[i] = False
        help()
        return result
        
            
        