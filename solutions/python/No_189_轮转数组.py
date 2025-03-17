# LeetCode No.189 轮转数组
# 题目链接: https://leetcode.cn/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150


from typing import List

#方法一：翻转数组
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(i:int, j: int)-> None:
            while i< j:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1

        n = len(nums)
        k%=n
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
        
#方法二：暴力破解     
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < k:
            last = nums[len(nums)-1]
            nums.insert(0,last)
            nums[len(nums)-1:] = []
            i+=1
            
            
            
        
            
        