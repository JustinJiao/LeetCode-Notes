# LeetCode No.94 二叉树的中序遍历
# 题目链接:https://leetcode.cn/problems/binary-tree-inorder-traversal/description/
from typing import Optional,List
import sys
import ast

class ListNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next
#方法一：
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def help(cur,result):
            if not cur:
                return
            help(cur.left,result)
            result.append(cur.val)
            help(cur.right,result)
        help(root,result)
        return result
    
            
            
        
            
        