# LeetCode No.236 二叉树的最近公共祖先
# 题目链接:https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Definition for a binary tree node.
#方法一: 递归
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def help(cur,p,q):
            if not cur:
                return None
            if cur == p or  cur == q:
                return cur
            left = help(cur.left,p,q)
            right = help(cur.right,p,q)

            if left and right:
                return cur

            if left and not right:
                return left
            elif not left and right:
                return right
            else:
                return None
        return help(root,p,q)