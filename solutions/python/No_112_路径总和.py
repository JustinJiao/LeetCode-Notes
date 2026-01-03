# LeetCode No.112 路径总和
# 题目链接: https://leetcode.cn/problems/path-sum/description/
# Definition for a binary tree node.
from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def help(cur,result):
            if not cur:
                return False
            result += cur.val
            if not cur.left and not cur.right:
                return result == targetSum
            if cur.left:
                left = help(cur.left,result)
                if left:
                    return True
            if cur.right:
                right = help(cur.right,result)
                if right:
                    return True
            return False
        return help(root,0)