# LeetCode No.018 四数之和
# 题目链接: https://leetcode.cn/problems/4sum/description/

from typing import List

#方法一：用双指针
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i >0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > target and nums[i] >0 and target > 0:
                break
            for j in range(i+1,len(nums)):
                if j-1 != i and nums[j] == nums[j-1]:
                    continue
                if nums[i]+nums[j] > target and target > 0:
                    break
                left = j +1
                right = len(nums)-1
                while left < right:
                    sum_ = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum_ > target:
                        right -= 1
                    elif sum_ < target:
                        left += 1
                    else:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left +=1
                        while left < right and nums[right] == nums[right-1]:
                            right -=1
                        left += 1
                        right -= 1
                        
        return result
        
            
        