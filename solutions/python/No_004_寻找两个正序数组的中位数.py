# LeetCode No.004 寻找两个正序数组的中位数
# 题目链接: https://leetcode.cn/problems/median-of-two-sorted-arrays/description/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        m = len(nums1)
        n = len(nums2)
        left_num = (m + n +1) //2
        left,right = 0,m
        while left <= right:
            i = (left + right) //2
            j = left_num - i
            #判断边界
            l1 = nums1[i-1] if i >0 else float('-inf')
            l2 = nums2[j-1] if j > 0 else float('-inf')
            r1 = nums1[i] if i < m else float('inf')
            r2 = nums2[j] if j < n else float('inf')

            #判断是否满足条件
            if l1 <= r2 and l2 <= r1:
                if (m+n) %2 == 1:
                    return max(l1,l2)
                else:
                    return ((max(l1,l2) + min(r1,r2)) /2)
            elif l1 > r2:
                right = i-1
            else:
                left = i +1