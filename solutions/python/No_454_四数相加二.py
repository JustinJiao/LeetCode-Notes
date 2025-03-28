# LeetCode No.454 四数相加二
# 题目链接: https://leetcode.cn/problems/4sum-ii/description/

from typing import List

#方法一：使用Counter计数
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        from collections import Counter
        A = Counter()
        n = len(nums1)
        count = 0
        for i in range(n):
            for j in range(n):
                A[nums1[i]+nums2[j]] +=1

        for j in nums3:
            for k in nums4:
                if -(j+k) in A:
                    count += A[-(j+k)]
        return count
        
        
            
        