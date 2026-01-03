# LeetCode No.538 把er
# 题目链接:https://leetcode.cn/problems/trim-a-binary-search-tree/description/

from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
            def help(cur):
                if not cur:
                    return None
                if cur.val < low:
                    return help(cur.right)
                if cur.val > high:
                    return help(cur.left)
                cur.left = help(cur.left)
                cur.right= help(cur.right)
                return cur
            return help(root)