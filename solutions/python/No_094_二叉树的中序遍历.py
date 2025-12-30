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
    
#方法二：遍历
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        cur = root
        while cur or stack:
            if cur :
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        return result
        
#方法三：空指针遍历
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                stack.append(None)
                if node.left:
                    stack.append(node.left)
            else:
                node = stack.pop()
                result.append(node.val)
        return result
## boolean标记法
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        if root:
            stack.append((root,False))
        while stack:
            node,visted = stack.pop()
            if visted:
                result.append(node.val)
                continue
            if node.right:
                stack.append((node.right,False))
            stack.append((node,True))
            if node.left:
                stack.append((node.left,False))
        return result