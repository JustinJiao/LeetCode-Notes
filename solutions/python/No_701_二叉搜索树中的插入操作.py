# LeetCode No.700 二叉搜索树中的搜索
# 题目链接:https://leetcode.cn/problems/search-in-a-binary-search-tree/description/
from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def help(cur):
            if not cur or cur.val == val:
                return cur
            if cur.val > val:
                return help(cur.left)
            else:
                return help(cur.right)

        return help(root)