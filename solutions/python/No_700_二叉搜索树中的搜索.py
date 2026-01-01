# LeetCode No.700 二叉搜索树中的插入操作
# 题目链接:https://leetcode.cn/problems/insert-into-a-binary-search-tree/description/

from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def help(cur):
            if not cur:
                node = TreeNode(val)
                return node
            if cur.val < val:
                cur.right = help(cur.right)
            if cur.val > val:
                cur.left = help(cur.left)
            return cur
        return help(root)