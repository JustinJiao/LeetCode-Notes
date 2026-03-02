# LeetCode No.236 二叉树的最近公共祖先
# 题目链接:https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Definition for a binary tree node.
#方法一: 递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def help(cur):
            if not cur:
                return None
            left = help(cur.left) #递归左子树
            right = help(cur.right) #递归右子树
            if cur == p or cur == q: #如果当前节点是p或者q,就返回当前节点
                return cur
            if left and right:#如果左子树和右子树都不为空,说明p和q分别在左右子树中,所以当前节点就是最近公共祖先
                return cur
            if left:#如果左子树不为空,说明p和q都在左子树中,所以返回左子树的结果
                return left
            if right:#如果右子树不为空,说明p和q都在右子树中,所以返回右子树的结果
                return right
            return None
        return help(root)
            
            