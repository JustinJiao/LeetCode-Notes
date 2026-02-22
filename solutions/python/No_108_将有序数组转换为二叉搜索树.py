# LeetCode No.108 将有序数组转换为二叉搜索树
# 题目链接: https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/
from typing import Optional,List
# Definition for a binary tree node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def help(left,right):
            if left > right:
                return None
            mid = (left +right) //2
            cur = TreeNode(nums[mid])
            cur.left = help(left,mid-1)
            cur.right = help(mid +1, right)
            return cur
        return help(0,len(nums)-1)