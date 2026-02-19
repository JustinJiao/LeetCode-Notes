# LeetCode No 101 对称二叉树
# 题目链接:https://leetcode.cn/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def help(left,right):
            if not left and not right:
                return True
            if not left and right:
                return False
            if left and not right:
                return False
            if left.val != right.val:
                return False
            inside = help(left.right,right.left)
            outside = help(left.left,right.right)
            return inside and outside
        return help(root.left,root.right)