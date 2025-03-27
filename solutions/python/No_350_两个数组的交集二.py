# LeetCode No.350 两个数组的交集二
# 题目链接: https://leetcode.cn/problems/intersection-of-two-arrays-ii/submissions/616185829/

from typing import List
        
#方法一：哈希表
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import defaultdict
        dic = defaultdict(int)
        result = []
        for i in nums1:
            dic[i] +=1
        for i in nums2:
            if i in dic:
                dic[i] -=1
                result.append(i)
                if dic[i] == 0:
                    del dic[i]
        return result
                
#方法二：数组
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = [0]*1001
        n2 = [0]*1001
        result = []
        for i in nums1:
            n1[i]+=1
        for i in nums2:
            n2[i] +=1
        for i in range(1001):
            if n1[i]*n2[i]>0:
                for _ in range(min(n1[i],n2[i])):
                    result.append(i)
        return result

            
            
        
            
        