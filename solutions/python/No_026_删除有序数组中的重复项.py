# LeetCode No.26 删除有序数组中的重复项
# 题目链接: https://leetcode.cn/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150


from typing import List

#方法一：暴力破解
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = []
        i = 0
        while i < len(nums):      # O(N)
            if nums[i] in result: # O(N)
                nums.pop(i)       # O(N)
                continue
            else:
                result.append(nums[i]) #O(1)
                i+=1
        return len(result)
        
#方法二，双指针快慢指针
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left,right = 0,1
        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
                right +=1
        return left +1
        
            
        