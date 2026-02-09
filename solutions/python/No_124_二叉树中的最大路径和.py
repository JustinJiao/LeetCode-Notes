# LeetCode No.124 二叉树中的最大路径和
# 题目链接: https://leetcode.cn/problems/binary-tree-maximum-path-sum/description/

# 方法一：递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float('-inf')
        def dfs(cur):
            nonlocal result
            if not cur:
                return 0
            left = max(dfs(cur.left),0)
            right = max(dfs(cur.right),0)
            result = max(result,cur.val + left + right)
            cur_max = cur.val + max(left,right)
            return cur_max
        dfs(root)
        return result
            