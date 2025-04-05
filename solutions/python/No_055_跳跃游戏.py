# LeetCode No.55 跳跃游戏
# 题目链接: https://leetcode.cn/problems/jump-game/description/

from typing import List

#方法一：贪心
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        i = 0
        if len(nums) == 1:
            return True
        while i <= cover:
            cover = max(cover,i+nums[i])
            if cover >= len(nums)-1:
                return True
            i+=1
        return False
            
        