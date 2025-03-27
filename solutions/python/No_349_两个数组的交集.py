# LeetCode No.349 两个数组的交集
# 题目链接: https://leetcode.cn/problems/intersection-of-two-arrays/description/

from typing import List

#方法一：set
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = set(nums1)
        n2 = set(nums2)
        return list(n1 & n2)
        
        
#方法二：哈希表
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
       from collections import defaultdict
       dic = defaultdict(int)
       result = set()
       for i in nums1:
            dic[i] +=1

       for i in nums2:
            if i in dic:
                result.add(i)
                del dic[i]
       return list(result)
   
#方法三：数组
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        c1 = [0]*1001
        c2 = [0]*1001
        for i in nums1:
            c1[i] +=1
        for i in nums2:
            c2[i] +=1
        for i in range(1001):
            if c1[i] * c2[i] >0:
                result.append(i)
        return result

            
            
        
            
        