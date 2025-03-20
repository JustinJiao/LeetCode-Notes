# LeetCode No.27 移除元素
# 题目链接: https://leetcode.cn/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150


from typing import List

#方法一：使用内置函数
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
            #print(nums)
        return len(nums)

#方法二：双指针
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for right in range(len(nums)):
            if(nums[right]!= val):
                nums[left] = nums[right]
                left +=1
        return left

        
        
        
            
        