# LeetCode No.114 二叉树展开为链表
# 题目链接: https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur  = root
        while cur:
            if cur.left:
                prev = cur.left
                while prev.right:
                    prev = prev.right
                
                prev.right = cur.right

                cur.right = cur.left
                cur.left = None
            cur = cur.right
        return root
