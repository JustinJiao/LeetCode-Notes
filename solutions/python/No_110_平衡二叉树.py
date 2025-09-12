# LeetCode No.110 平衡二叉树
# 题目链接: https://leetcode.cn/problems/balanced-binary-tree/description/

from typing import Optional,List
import sys
import ast

class ListNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next
#方法一：递归
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def help(cur):
            if not cur:
                return 0
            left = help(cur.left)
            right = help(cur.right)
            if left == -1 or right == -1 or abs(left-right) >1:
                return -1
            return max(left,right)+1
        return help(root) != -1