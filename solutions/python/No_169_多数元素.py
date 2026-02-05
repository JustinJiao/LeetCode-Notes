# LeetCode No.169 多数元素
# 题目链接: https://leetcode.cn/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150

from typing import List

#方法一：字典
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        dic = defaultdict(int)
        target = len(nums) // 2
        for num in nums:
            dic[num]+=1
            if dic[num] > target:
                return num

        
#方法二：寻找中位数
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        left,right = 0,len(nums)-1
        mid = (left+right) // 2
        return nums[mid]
        
        
            
        