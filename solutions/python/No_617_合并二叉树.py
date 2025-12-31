# LeetCode No.617 合并二叉树
# 题目链接:https://leetcode.cn/problems/merge-two-binary-trees/description/

from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def help(left,right):
            if not left:
                return right
            if not right:
                return left
            value = left.val + right.val
            root = TreeNode(value)
            left_tree = help(left.left,right.left)
            right_tree = help(left.right,right.right)
            root.left = left_tree
            root.right = right_tree
            return root
        return help(root1,root2)