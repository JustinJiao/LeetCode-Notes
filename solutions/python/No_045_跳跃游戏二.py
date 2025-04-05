# LeetCode No.45 跳跃游戏二
# 题目链接: https://leetcode.cn/problems/jump-game-ii/description/

from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        cur = 0
        result = 0
        next_ = 0
        for i in range(len(nums)-1):
            next_ = max(next_,i + nums[i])
            if i == cur:            ##到达现在目前的cover的结尾了
                result +=1
                cur = next_
        return result
        
        
        
            
        