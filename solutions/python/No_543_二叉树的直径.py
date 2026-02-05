# LeetCode No.543 二叉树的直径
# 题目链接: https://leetcode.cn/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def help(cur):
            nonlocal result
            if not cur:
                return 0
            left = help(cur.left)
            right = help(cur.right)
            result = max(result,left+right)
            return max(left,right) +1
        help(root)
        return result