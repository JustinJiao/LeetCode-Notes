# LeetCode No.209 长度最小的子数组
# 题目链接: https://leetcode.cn/problems/minimum-size-subarray-sum/description/


import bisect
from typing import List

#方法一：双指针（滑动窗口）
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum = 0
        result = float('inf') #最大的数 float('-inf')是无穷小
        subList = 0
        for right in range(len(nums)):
            sum += nums[right]
            while sum >= target:
                subList = right - left+1
                result = min(result,subList)
                sum -= nums[left]
                left += 1
        if result > len(nums):
            return 0
        return result

        
        
#方法二：前缀和+二分法    
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sums= [0]
        n = len(nums)
        ans = n+1
        for i in range(n):
            sums.append(sums[-1]+nums[i]) ## sums[-1]是sums最后一个元素
        
        for i in range(1,n+1):
            findT = target + sums[i-1]
            bound = bisect.bisect_left(sums,findT)
            if bound != len(sums):
                ans = min(ans,bound-(i-1))
        if ans == n+1:
            return 0
        return ans
            
            
            
        
            
        