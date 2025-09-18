# LeetCode No 100 相同的树
# 题目链接:https://leetcode.cn/problems/same-tree/

from typing import Optional,List
import sys
import ast

class ListNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#方法一：
# Definition for a binary tree node.
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def help(left,right):
            if left and not right:
                return False
            if not left and right:
                return False
            if not left and not right:
                return True
            if left.val != right.val:
                return False
            l = help(left.left,right.left)
            r = help(left.right,right.right)
            return l and r
        return help(p,q)