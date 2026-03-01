# LeetCode No.496 下一个更大元素一
# 题目链接: https://leetcode.cn/problems/next-greater-element-i/description/

#方法一：单调栈
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        stack = []
        result = [0] * len(nums1)
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                dic[nums2[stack[-1]]] = nums2[i]
                stack.pop()
            stack.append(i)

        for i in range(len(nums1)):
            result[i] = dic.get(nums1[i],-1)
        return result