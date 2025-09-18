# LeetCode No.404 左叶子之和
# 题目链接: https://leetcode.cn/problems/sum-of-left-leaves/description/

from typing import List,Optional

#方法一：递归
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftValue = self.sumOfLeftLeaves(root.left)
        if root.left and not root.left.left and not root.left.right:
            leftValue = root.left.val
        rightValue = self.sumOfLeftLeaves(root.right)
        return leftValue + rightValue
            
            
        
            
        