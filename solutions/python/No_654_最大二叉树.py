# LeetCode No.654 最大二叉树
# 题目链接:https://leetcode.cn/problems/maximum-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional,List
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def help(num):
            if not num:
                return None
            rootvalue = max(num)
            root = TreeNode(val = rootvalue)
            index = num.index(rootvalue)

            left_tree = num[:index]
            right_tree = num[index+1:]

            root.left = help(left_tree)
            root.right = help(right_tree)

            return root
        return help(nums)