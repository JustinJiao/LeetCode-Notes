# LeetCode No.450 删除二叉搜索树中的节点
# 题目链接:https://leetcode.cn/problems/delete-node-in-a-bst/description/
from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def help(cur):
            if not cur:
                return None
            if cur.val == key:
                if not cur.left and not cur.right:
                    return None
                elif cur.left and not cur.right:
                    return cur.left
                elif not cur.left and cur.right:
                    return cur.right
                else:
                    template = cur.right
                    while template.left:
                        template = template.left
                    template.left = cur.left
                    return cur.right
            if key > cur.val:
                cur.right = help(cur.right)
            if key < cur.val:
                cur.left = help(cur.left)
            return cur
        return help(root)