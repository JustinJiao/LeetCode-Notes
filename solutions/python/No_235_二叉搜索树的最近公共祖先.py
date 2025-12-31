# LeetCode No.235 二叉搜索树的最近公共祖先
# 题目链接:https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
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
            if cur.val > p.val and cur.val > q.val:
                left = help(cur.left,p,q)
                if left:
                    return left
            if cur.val < p.val and cur.val < q.val:
                right = help(cur.right,p,q)
                if right:
                    return right
            return cur
        return help(root,p,q)