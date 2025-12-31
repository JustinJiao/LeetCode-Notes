# LeetCode No.530 二叉搜索树的最小绝对差
# 题目链接:https://leetcode.cn/problems/minimum-absolute-difference-in-bst/description/

from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = float('inf')
        prev = None
        def help(cur):
            if not cur:
                return None
            nonlocal result,prev
            help(cur.left)
            if prev:
                result = min(result,cur.val - prev.val)
            prev = cur
            help(cur.right)
        help(root)
        return result