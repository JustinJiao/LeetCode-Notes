# LeetCode No.27 移除元素
# 题目链接: https://leetcode.cn/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150


from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
            #print(nums)
        return len(nums)
        
        
        
            
        