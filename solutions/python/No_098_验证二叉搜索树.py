# LeetCode No.98 验证二叉搜索树
# 题目链接:https://leetcode.cn/problems/validate-binary-search-tree/description/

#方法一：递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        max_val = float('-inf')
        def dfs(cur):
            nonlocal max_val
            if not cur:
                return True
            left = dfs(cur.left)
            if cur.val > max_val:
                max_val = cur.val
            else:
                return False
            right = dfs(cur.right)
            return left and right
        return dfs(root)
            
