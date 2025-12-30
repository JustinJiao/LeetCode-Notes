# LeetCode No.104 从中序与后序遍历序列构造二叉树
# 题目链接:https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
# Definition for a binary tree node.
from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def help(inorder,postorder):
            if not postorder:
                return None
            value = postorder[-1]
            root = TreeNode(val = value)

            index = inorder.index(value)
            left_inorder = inorder[:index]
            right_inorder = inorder[index+1:]

            left_postorder = postorder[:len(left_inorder)]
            right_postorder = postorder[len(left_inorder):len(postorder)-1]

            root.left = help(left_inorder,left_postorder)
            root.right = help(right_inorder,right_postorder)
            return root
        return help(inorder,postorder)
        